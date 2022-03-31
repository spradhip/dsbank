import pulsar,time
from dotenv import load_dotenv
import os

load_dotenv()

service_url = os.getenv('service_url')
token = os.getenv('token')
topic = os.getenv('topic_card_cdc')

client = pulsar.Client(service_url, authentication=pulsar.AuthenticationToken(token))
consumer = client.subscribe(topic, 'data-0ca9cde2-7cd1-4e7f-93ec-af01678d6f34-dsbank2.card_accounts_by_card_no')

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