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

class BankTransactionsRecord(Record):

    account_no = String()
    account_type = String()
    transaction_id = String()
    date_time = String()
    amount = Float()
    balance = Float()
    external_account_number = String()
    external_account_name = String()
    description = String()
    status = String()
    transaction_type = String()
    customer_id = String()

producer = client.create_producer(topic=topic,schema=AvroSchema(BankTransactionsRecord))

for i in range(1,20):

    time.sleep(1)

    fake = Faker()

    account_no = str(random.randint(1, 10000))
    account_type = random.choice(['CHECKING', 'SAVINGS'])
    transaction_id = str(uuid.uuid1())
    customer_id = str(random.randint(123456, 123456))

    date_time = fake.date_between_dates(date_start=datetime(2020, 1, 1),date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')
    amount = round(random.uniform(0.00, 1000.00), 2)
    balance = round(random.uniform(1.00, 10000.00), 2)
    external_account_number = ""
    external_account_name = ""
    description = ""
    status = random.choice(['PENDING', 'CONFIRMED'])
    transaction_type = ''

    if (account_type in ['SAVINGS']):
        transaction_type = 'TRANSFER'
        amount = round(random.uniform(-1000.00, 1000.00), 2)

    if (account_type in ['CHECKING']):
        transaction_type = random.choice(['DEPOSIT', 'WITHDRAWL', 'TRANSFER'])
        if (transaction_type in ['WITHDRAWL']):
            amount = round(random.uniform(-1000.00, 0.00), 2)
        if (transaction_type in ['TRANSFER']):
            amount = round(random.uniform(-1000.00, 1000.00), 2)

    print("ingesting to topic bank_transactions..." + str(i) + " " + transaction_id)
    producer.send(BankTransactionsRecord(account_no=account_no, account_type=account_type,transaction_id=transaction_id, date_time = date_time,amount=amount,balance=balance,external_account_number=external_account_number,external_account_name=external_account_name,description=description,status=status,transaction_type=transaction_type,customer_id=customer_id))

client.close()