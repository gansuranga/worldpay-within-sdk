from consumer import SampleConsumer
import ttypes as types
import wpwithin

hceCard = types.HCECard(firstName='Bilbo', lastName='Baggins', expMonth=11, expYear=2018, cardNumber='5555555555554444', cardType='Card', cvc='113')

out = wpwithin.createClient("127.0.0.1", 8778, True)

client = out['client']
agent = out['rpc']

consumer = SampleConsumer(client, agent, hceCard)

consumer.client.setup("Python3 test consumer", "Python3 sample consumer device")

print("Finding myself...")

device = consumer.client.getDevice()
if device is None:
    print("No devices found")

else:
    print("Successfully found itself:")
    a = """uid: {0.uid}
name: {0.name}
description: {0.description}
ipv4: {0.ipv4Address}"""
    print(a.format(device, device.services))

    print("Getting device details...")
    
    serviceMessage = consumer.getDeviceDetails()

    if serviceMessage is not None:
        consumer.connectToDevice(serviceMessage)
        consumer.purchaseFirstServiceFirstPrice(1)
