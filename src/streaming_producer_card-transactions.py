import pulsar,time
from pulsar.schema import *
from faker import Faker
import random
from datetime import datetime
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

service_url = os.getenv('service_url')
token = os.getenv('token')
topic = os.getenv('topic')

client = pulsar.Client(service_url,authentication=pulsar.AuthenticationToken(token))

class CardTransactionsRecord(Record):

    card_no = String()
    card_name = String()
    transaction_id = String()
    date_time = String()
    amount = Float()
    merchant = String()
    description = String()
    location = String()
    status = String()
    type = String()
    category = String()
    customer_id = String()


producer = client.create_producer(topic=topic,schema=AvroSchema(CardTransactionsRecord))

for i in range(1,20):

    time.sleep(1)

    fake = Faker()

    card_no = str(random.randint(1, 10000))
    card_name = random.choice(['AMEX', 'VISA', 'MASTERCARD'])
    transaction_id = str(uuid.uuid1())
    customer_id = str(random.randint(123456, 123456))
    date_time = fake.date_between_dates(date_start=datetime(2020, 1, 1),date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')
    amount = round(random.uniform(0.00, -200.00), 2)
    merchant = random.choice(["AMAZON", "KROGER", "MACYS", "COSTCO", "TARGET", "WALMART", "CHICKFILA", "HOMEGOODS", "MICHAELS", "CHIPOTLE","PIZZAHUT", "DOMINOS"])
    location = ""
    description = ""
    status = random.choice(['PENDING', 'CONFIRMED'])
    category = ""
    type = random.choice(['DEBIT'])


    if (merchant in ["AMAZON"]):
        category = "ECOMMERCE"
    if (merchant in ["COSTCO"]):
        category = "WHOLESALE"
    if (merchant in ["KROGER"]):
        category = "GROCERY"
    if (merchant in ["WALMART", "TARGET", "HOMEGOODS", "MACYS", "MICHAELS"]):
        category = "DEPT STORE"
    if (merchant in ["CHIPOTLE", "PIZZAHUT", "DOMINOS","CHICKFILA"]):
        category = "RESTAURANT"

    print("ingesting to topic card_transactions..." + str(i) + " " + transaction_id)
    producer.send(CardTransactionsRecord(card_no=card_no, card_name=card_name,transaction_id=transaction_id, date_time = date_time,amount=amount,merchant=merchant,description=description,location=location,status=status,type=type,category=category,customer_id=customer_id))

client.close()