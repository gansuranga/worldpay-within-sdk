import time
from wpwithin_python import Error, CommonPSPKeys, WorldpayPSPKeys, WP_PSP_NAME


class SampleConsumer:
    def __init__(self, client, agent, hce_card):
        self.client = client
        self.agent = agent
        self.hce_card = hce_card

    def get_device_details(self):
        try:
            service_messages = self.client.device_discovery(8000)
        except Error as err:
            print("deviceDiscovery.callback.err: " + err.message)
            raise err
        if len(service_messages) == 0:
            print("Did not discover any devices on the network.")
            return None

        device_count = len(service_messages)
        print("Discovered {0} devices on the network.".format(len(service_messages)))
        print("Devices:")

        for i in range(device_count):
            device_log = '''Description: {0.device_description}
            Hostname: {0.hostname}
            Port: {0.port_number}
            Server ID: {0.server_id}
            URL Prefix: {0.url_prefix}
            Scheme: {0.scheme}'''.format(service_messages[i])

            print(device_log)

        # Connect to first device
        return service_messages[0]

    def connect_to_device(self, service_message):
        psp_config = {
            CommonPSPKeys.psp_name: WP_PSP_NAME,
            WorldpayPSPKeys.wp_api_endpoint: "https://api.worldpay.com/v1",
        }
        try:
            self.client.init_consumer('http://',
                                      service_message.hostname,
                                      service_message.port_number,
                                      service_message.url_prefix,
                                      service_message.server_id,
                                      self.hce_card,
                                      psp_config)
        except Error as err:
            print("initConsumer.callback.err: " + err.message)
            raise err
        else:
            print("Initialised consumer.")

    def get_first_available_service(self):
        try:
            service_details = self.client.request_services()
        except Error as err:
            print("requestServices.callback.err: " + err.message)
            raise err
        if len(service_details) > 0:
            service = service_details[0]
            print("Service:")
            print("Id: {0}".format(service.service_id))
            print("Description: {0}".format(service.service_description))
            print("----------")
            return service.service_id

    def get_service_first_price(self, service_id):
        try:
            prices = self.client.get_service_prices(service_id)
        except Error as err:
            print("requestServicePrices.callback.err: " + err.message)
            raise err

        if len(prices) > 0:
            price = prices[0]
            print_message = """Price details for Service Id {0}:
            Id: {1.price_id}
            Description: {1.description}
            UnitId: {1.unit_id}
            Unit Description: {1.unit_description}
            Price per Unit:
            \tAmount: {1.price_per_unit.amount}
            \tCurrency Code: {1.price_per_unit.currency_code}
            ----------
            """.format(service_id, price)

        else:
            raise Error("Did not receive any service prices :/")

        return price

    def get_service_price_quote(self, service_id, number_of_units, price_id):
        try:
            price_response = self.client.select_service(service_id, number_of_units, price_id)
        except Error as err:
            print("selectService.callback.err: " + err.message)
            raise err

        if price_response is None:
            print("Did not receive total price response from selectService()")
            return None

        return price_response

    def purchase_first_service_first_price(self, number_of_units):

        service_id = self.get_first_available_service()

        price_id = self.get_service_first_price(service_id).price_id

        price_response = self.get_service_price_quote(service_id, number_of_units, price_id)

        try:
            response = self.client.make_payment(price_response)
        except Error as err:
            print("makePayment.callback.err: " + err.message)
            raise err

        if response is None:
            print("Did not receive correct response to make payment")
            return None

        time.sleep(15)

        print("sending callback")
        token = self.client.begin_service_delivery(service_id,
                                                   response.service_delivery_token,
                                                   number_of_units)

        print("Shutting down...")

        self.client.end_service_delivery(service_id,
                                         token,
                                         number_of_units)

        self.agent.kill()
