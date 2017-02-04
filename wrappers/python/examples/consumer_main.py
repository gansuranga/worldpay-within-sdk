from consumer import SampleConsumer
from wpwithin_python import WPWithin, HCECard

hce_card = HCECard(first_name='Bilbo',
                   last_name='Baggins',
                   exp_month=11,
                   exp_year=2018,
                   card_number='5555555555554444',
                   card_type='Card',
                   cvc='113')

client = WPWithin("127.0.0.1", 8778, True)

consumer = SampleConsumer(client, hce_card)

consumer.client.setup("Python3 test consumer", "Python3 sample consumer device")

print("Finding myself...")

device = consumer.client.get_device()
if device is None:
    print("No devices found")

else:
    print("Successfully found itself:")
    a = """uid: {0.uid}
name: {0.name}
description: {0.description}
ipv4: {0.ipv4address}"""
    print(a.format(device, device.services))

    print("Getting device details...")

    service_message = consumer.get_device_details()

    if service_message is not None:
        consumer.connect_to_device(service_message)
        consumer.purchase_first_service_first_price(1)

consumer.client.shutdown()