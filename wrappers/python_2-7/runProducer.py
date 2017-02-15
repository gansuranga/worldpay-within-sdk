import WPWithinWrapperImpl
import WWTypes
import time



class TheEventListener():
    def __init__(self):
        print "Inialised custom event listener"

    def beginServiceDelivery(self, serviceId, serviceDeliveryToken, unitsToSupply):
        try:
            print "OVERRIDE: event from core - onBeginServiceDelivery()"
            print "ServiceID: {0}\n".format(serviceId)
            print "UnitsToSupply: {0}\n".format(unitsToSupply)
            print "SDT.Key: {0}\n".format(serviceDeliveryToken.key)
            print "SDT.Expiry: {0}\n".format(serviceDeliveryToken.expiry)
            print "SDT.Issued: {0}\n".format(serviceDeliveryToken.issued)
            print "SDT.Signature: {0}\n".format(serviceDeliveryToken.signature)
            print "SDT.RefundOnExpiry: {0}\n".format(serviceDeliveryToken.refundOnExpiry)
        except Exception as e:
            print "doBeginServiceDelivery failed: " + str(e)

    def endServiceDelivery(self, serviceId, serviceDeliveryToken, unitsReceived):
        try:
            print "OVERRIDE: event from core - onEndServiceDelivery()"
            print "ServiceID: {0}\n".format(serviceId)
            print "UnitsReceived: {0}\n".format(unitsReceived)
            print "SDT.Key: {0}\n".format(serviceDeliveryToken.key)
            print "SDT.Expiry: {0}\n".format(serviceDeliveryToken.expiry)
            print "SDT.Issued: {0}\n".format(serviceDeliveryToken.issued)
            print "SDT.Signature: {0}\n".format(serviceDeliveryToken.signature)
            print "SDT.RefundOnExpiry: {0}\n".format(serviceDeliveryToken.refundOnExpiry)
        except Exception as e:
            print "doEndServiceDelivery failed: " + str(e)


def run():
    try:
        print "WorldpayWithin Sample Producer (with callbacks)..."
        global wpw
        wpWithinEventListener = TheEventListener()
        # add listeners to the events
        # wpWithinEventListener.onBeginServiceDelivery += doBeginServiceDelivery
        # wpWithinEventListener.onEndServiceDelivery += doEndServiceDelivery		
        wpw = WPWithinWrapperImpl.WPWithinWrapperImpl(__file__, '127.0.0.1', 9055, True, wpWithinEventListener, 9095)
        wpw.setup("Producer Example", "Example WorldpayWithin producer")		
        svc = WWTypes.WWService();
        svc.setName("Car charger")
        svc.setDescription("Can charge your hybrid / electric car")
        svc.setId(1)
        ccPrice = WWTypes.WWPrice()
        ccPrice.setId(1)
        ccPrice.setDescription("Kilowatt-hour")
        ccPrice.setUnitDescription("One kilowatt-hour")
        ccPrice.setUnitId(1)
        ppu = WWTypes.WWPricePerUnit()
        ppu.setAmount(25)
        ppu.setCurrencyCode("GBP")
        ccPrice.setPricePerUnit(ppu)
        prices = {}
        prices[ccPrice.getId()] = ccPrice
        svc.setPrices(prices)

        ####################################################
        # For Worldpay online.worldpay.com - UNCOMMENT BELOW
        ####################################################
        # clientKey = "<client-key>"
        # serviceKey = "<service-key>"
        # apiEndpoint = "https://api.worldpay.com/v1"
        # onlineWordpayCredentials = {"psp_name":"worldpayonlinepayments","hte_public_key":clientKey, "hte_private_key": serviceKey, "api_endpoint":apiEndpoint, "merchant_client_key": clientKey, "merchant_service_key": serviceKey}
        # producerCredentials = onlineWordpayCredentials
        ####################################################

        ####################################################
        # For Worldpay Total / Securenet - UNCOMMENT BELOW
        ####################################################
        # secureNetId = "<securenetid>"
        # secureKey = "<securekey>"
        # publicKey = "<publickey>"
        # apiEndpoint = "https://gwapi.demo.securenet.com/api/"
        # securenetCredentials = {"psp_name":"securenet","developer_id":"12345678", "secure_key": secureKey, "api_endpoint":apiEndpoint, "public_key": publicKey, "secure_net_id":secureNetId, "app_version":"0.1", "merchant_client_key": publicKey, "merchant_service_key": secureKey,"hte_public_key":publicKey, "hte_private_key": secureKey}
        # producerCredentials = securenetCredentials
        ####################################################

        wpw.initProducer(producerCredentials)


        wpw.addService(svc)
        broadcastDuration = 20000
        durationSeconds = broadcastDuration / 1000
        wpw.startServiceBroadcast(broadcastDuration) #20000
        repeat = 0
        while repeat < durationSeconds:
            print "Producer Waiting " + str(durationSeconds - repeat) + " seconds to go..."
            time.sleep(1)
            repeat = repeat + 1
        print "Stopped broadcasting, RPC still running"
        repeat2 = 0
        while repeat2 < 99999999999:
            print "Producer keeping alive (to receive callbacks...)"
            time.sleep(1)
            repeat2 = repeat2 + 1        
    except WWTypes.WPWithinGeneralException as e:
        print e

run()
