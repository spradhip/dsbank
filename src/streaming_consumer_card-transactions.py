import pulsar,time
from dotenv import load_dotenv
import os

load_dotenv()

service_url = os.getenv('service_url')
token = os.getenv('token')
topic = os.getenv('topic')

client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(topic, 'card-transactions')

waitingForMsg = True
while waitingForMsg:
    msg = consumer.receive()
    try:
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))

        # acknowledging the message to remove from message backlog
        consumer.acknowledge(msg)
    except:
        print("Still waiting for a message...");

    time.sleep(1)

client.close()