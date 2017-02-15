#!/usr/bin/python

import ServiceAdapter
import EventServer
import rpc
from wpwithin.WPWithin import Client
import time
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import WWTypes
import logging
import json
import os


class WPWithinWrapperImpl(object):

    cachedClient = None
    logging.basicConfig(filename='worldpay-within-wrapper.log', level=logging.DEBUG)



    def __init__(self, programmeName, ipAddress, portNumber, startRpcCallbackAgent=False, wpWithinEventListener=None, eventListenerPort=0):

        self.killOrphanedRpcAgents(programmeName)
        self.portNumber = portNumber
        self.ipAddress = ipAddress
        self.eventListenerPort = eventListenerPort
        if startRpcCallbackAgent is not None and startRpcCallbackAgent != "" and startRpcCallbackAgent is True and eventListenerPort is not None and eventListenerPort != "":
            if eventListenerPort <= 0 or eventListenerPort > 65535:
                raise WWTypes.WPWithinGeneralException.WPWithinGeneralException("callback port must be >0 and <655535", None)
            # does taking out the assignment introduce a bug?
            EventServer.EventServer(wpWithinEventListener, self.ipAddress, eventListenerPort)
        self.rpcRunning = False
        self.rpcProcess = self.startRpc(self.ipAddress, self.portNumber, self.eventListenerPort)
        self.logRpcAgent(self.rpcProcess.pid, programmeName)
        self.setClientIfNotSet()

    def killOrphanedRpcAgents(self, programmeName):
        jsonFile = './track-rpc-agent.json'
        fileSize = os.stat(jsonFile).st_size
        logging.info('size of track file: ' + str(fileSize))
        with open(jsonFile) as json_data:
            logging.info('size of track file: ' + str(fileSize))
            if fileSize != 0:
                d = json.load(json_data)
                if d is not None:
                    logging.debug(json.dumps(d))
                    rpcAgents = d['track']
                    for i in rpcAgents:
                       if i['rpcAgentName'] == programmeName: 
                          # kill the rpc agent
                          logging.info("An orphaned RpcAgent process ' + str(i['rpcProcess']) + ' was found from " + programmeName + ", attempting to kill")
                          os.system('ps -f -p ' + str(i['rpcProcess']) + ' | grep rpc-agent > /dev/null && kill ' + str(i['rpcProcess']))
                else:
                    logging.info("No orphaned RpcAgent processes from " + programmeName + " - couldn't read any Json data")
            else:
                logging.info("No orphaned RpcAgent processes from " + programmeName + " - no data in tracker file")

    def setClientIfNotSet(self):
        if self.cachedClient is None:
            self.cachedClient = self.openRpcListener()

    def startRpc(self, ipAddress, port, eventListenerPort):
        if(self.rpcRunning is False):
            logging.info("Starting Port: " + str(port))
            process = rpc.startRPC(ipAddress, port, eventListenerPort)
            self.rpcRunning = True
            # Give time for the service to start
            time.sleep(5)
            return process


    def logRpcAgent(self, rpcProcessId, programmeName):
        jsonFile = 'track-rpc-agent.json'
        fileSize = os.stat(jsonFile).st_size
        with open(jsonFile, 'w+') as json_data:
            if fileSize != 0 and json_data is not None:
                isJason = True
                d = None
                try:
                    d = json.load(json_data)
                except ValueError, e:
                    isJson = False 
                if d is not None: 
                    logging.debug("Adding process Id")
                    rpcAgents = d['track']
                    rpcAgents.append({ "rpcAgentName": programmeName, "rpcProcess": rpcProcessId }) 
                else:
                    logging.debug("Overwriting process Id")
                    rpcAgents = { "rpcAgentName": programmeName, "rpcProcess": rpcProcessId }
                json.dump({"track": [ rpcAgents ]}, json_data)
            else:
                rpcAgents = { "rpcAgentName": programmeName, "rpcProcess": rpcProcessId } 
                json.dump({"track": [ rpcAgents ]}, json_data)

    def getClient(self):
        self.setClientIfNotSet()
        return self.cachedClient

    def openRpcListener(self):
        try:
            # Make socket
            transport = TSocket.TSocket(self.ipAddress, self.portNumber)
            # Buffering is critical. Raw sockets are very slow
            transport = TTransport.TBufferedTransport(transport)
            # Wrap in a protocol
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            # Create a client to use the protocol encoder
            client = Client(protocol)
            # Connect!
            transport.open()
            logging.info("STARTED connection to SDK via RPC thrift")
            return client
        except Exception as e:
            logging.info("Error: Couldn't open the RpcListener: " + str(e))
            raise WWTypes.WPWithinGeneralException("Error: Couldn't open the RpcListener", e)

    def setup(self, deviceName, deviceDescription):
        try:
            self.getClient().setup(deviceName, deviceDescription)
            logging.info("SHOULD HAVE SETUP DEVICE: (" + str(deviceName) + "), (" + str(deviceDescription) + ")")
        except Exception as e:
            logging.info("Error - Failure to setup DEVICE in the wrapper, could be the new config file is missing - gotcha!: " + str(e))
            raise WWTypes.WPWithinGeneralException("Error - Failure to setup DEVICE in the wrapper, could be the new config file is missing - gotcha!: ", e)

    def addService(self, theService):
        try:
            self.getClient().addService(ServiceAdapter.convertWWService(theService))
            logging.info('SHOULD HAVE ADDED SERVICE')
        except Exception as e:
            logging.info("Error - Add service to producer failed with Rpc call to the SDK lower level: " + str(e))
            raise WWTypes.WPWithinGeneralException("Error - Add service to producer failed with Rpc call to the SDK lower level", e)

    def removeService(self, svc):
        try:
            self.getClient().removeService(ServiceAdapter.convertWWService(svc))
        except Exception as e:
            logging.info("Removal of service failed in the wrapper: " + str(e))
            raise WWTypes.WPWithinGeneralException("Removal of service failed in the wrapper: ", e)

    def requestServices(self):
        try:
            return ServiceAdapter.convertServiceDetailList(self.getClient().requestServices())
        except Exception as e:
            logging.info("Request services failed in wrapper: " + str(e))
            raise WWTypes.WPWithinGeneralException("Request services failed in wrapper", e)

    def getDevice(self):
        try:
            device = self.getClient().getDevice()
            wwDevice = ServiceAdapter.convertDevice(device)
            logging.info('SHOULD HAVE RUN GET DEVICE')
            return wwDevice
        except Exception as e:
            logging.info("Get device in wrapper failed: " + str(e))
            raise WWTypes.WPWithinGeneralException("Get device in wrapper failed", e)

    def stopRPCAgent(self):
        logging.info('SHOULD STOP RPC AGENT')
        try:
            self.rpcProcess.kill()
        except Exception as e:
            logging.info("Could not stop the RPC service: " + str(e))
            raise WWTypes.WPWithinGeneralException("Could not stop the RPC service", e)

    def deviceDiscovery(self, timeout):
        logging.info('STARTING DO DEVICE DISCOVERY')
        try:
            svcMsgs = ServiceAdapter.convertServiceMessages(self.getClient().deviceDiscovery(timeout))
            logging.info('Finished device discovery')
            return svcMsgs
        except Exception as e:
            logging.info("Failed device discovery in wrapper: " + str(e))
            raise WWTypes.WPWithinGeneralException("Failed device discovery in wrapper", e)

    def initConsumer(self, scheme, hostname, port, urlPrefix, serverId, hceCard, pspConfig):
        try:
            self.getClient().initConsumer(scheme, hostname, port, urlPrefix, serverId, ServiceAdapter.convertWWHCECard(hceCard), pspConfig)
        except Exception as e:
            logging.info("Initiating the consumer failed in the wrapper: " + str(e))
            raise WWTypes.WPWithinGeneralException("Initiating the consumer failed in the wrapper", e)

    def initProducer(self, pspConfig):
        try:
            self.getClient().initProducer(pspConfig)
            logging.info('SHOULD HAVE INIT THE PRODUCER')
        except Exception as e:
            logging.info("Initiating the producer failed in the wrapper: " + str(e))
            raise WWTypes.WPWithinGeneralException("Initiating the producer failed in the wrapper", e)

    def startServiceBroadcast(self, timeout):
        try:
            self.getClient().startServiceBroadcast(timeout)
            logging.info('SHOULD HAVE START SERVICE BROADCAST')
        except WWTypes.WPWithinGeneralException as e:
            print "Start service broadcast in wrapper failed: " + e

    def stopServiceBroadcast(self):
        try:
            self.getClient().stopServiceBroadcast()
        except WWTypes.WPWithinGeneralException as e:
            print "Stop service broadcast failed: " + e

    def getServicePrices(self, serviceId):
        try:
            return ServiceAdapter.convertServicePrices(self.getClient().getServicePrices(serviceId))
        except WWTypes.WPWithinGeneralException as e:
            print "Get Service Prices failed in wrapper: " + e

    def selectService(self, serviceId, numberOfUnits, priceId):
        try:
            return ServiceAdapter.convertTotalPriceResponse(self.getClient().selectService(serviceId, numberOfUnits, priceId))
        except WWTypes.WPWithinGeneralException as e:
            print "Select service failed in wrapper: " + e

    def makePayment(self, request):
        try:
            return ServiceAdapter.convertPaymentResponse(self.getClient().makePayment(ServiceAdapter.convertWWTotalPriceResponse(request)))
        except WWTypes.WPWithinGeneralException as e:
            print "Failed to make payment in the wrapper: " + e

    def beginServiceDelivery(self, serviceId, serviceDeliveryToken, unitsToSupply):
        try:
            print "Checking ServiceDelviery Input"
            if(serviceId is None):
                raise WWTypes.WPWithinGeneralException('Service Id cant be None')
            elif(serviceDeliveryToken is None):
                raise WWTypes.WPWithinGeneralException('serviceDeliveryToken cant be None')
            elif(unitsToSupply is None):
                raise WWTypes.WPWithinGeneralException('unitsToSupply cant be None')
            else:
                print "Input variables looked good " + str(serviceId) + " " + str(serviceDeliveryToken) + " " + str(unitsToSupply)
            csdt = ServiceAdapter.convertWWServiceDeliveryToken(serviceDeliveryToken)
            print "servicedeliverytoken converted: " + str(csdt)
            print "serviceId that's going to be consumed: " + str(serviceId)            
            sdt = self.getClient().beginServiceDelivery(serviceId, csdt, unitsToSupply)
            return ServiceAdapter.convertServiceDeliveryToken(sdt)
        except Exception as e:
            print "Failed to begin Service Delivery in the wrapper: " + str(e)

    def endServiceDelivery(self, serviceId, serviceDeliveryToken, unitsReceived):
        try:
            self.getClient().endServiceDelivery(serviceId, ServiceAdapter.convertWWServiceDeliveryToken(serviceDeliveryToken), unitsReceived)
        except Exception as e:
            print "Failed to end Service Delivery in the wrapper: " + str(e)
