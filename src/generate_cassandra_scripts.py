from datetime import datetime
from faker import Faker
import random
import uuid


def customer_scripts():

    print("customer scripts")

    fake = Faker()
    sql1 = "INSERT INTO dsbank.customer_profile(customer_id,first_name,last_name,dob,gender,email,phone_number,address1,city,state,zip,country,status_code) " \
          "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    for i in range (1,10):
        customer_no = customer_no
        first_name = fake.first_name().upper()
        last_name = fake.last_name().upper()
        dob = fake.date_between_dates(date_start=datetime(1950, 1, 1), date_end=datetime(2010, 12, 31)).strftime('%Y-%m-%d')
        gender_list = ['M', 'F']
        gender = random.choice(gender_list)
        email = fake.email()
        phone_number = fake.phone_number().split("x")[0]
        address = fake.address().upper()
        address1 = address.split()[0] + " " + address.split()[1]
        city = fake.city().upper()
        state = fake.state().upper()
        zipcode = fake.zipcode()
        country = 'USA'
        status_list = ['ACT', 'INA']
        status = random.choice(status_list)

        val1 = (customer_no, first_name, last_name, dob, gender, email, phone_number, address1, city, state, zipcode, country, status)
        print(val1)


def bank_account_scripts():
    print("bank account scripts")

    fake = Faker()

    sql = "INSERT INTO dsbank.bank_accounts_by_account_no(account_no,routing_no,date_created,balance,account_type,status,customer_id) " \
          "VALUES "

    account_no = str(random.randint(1, 10000))
    customer_id = str(random.randint(123456, 123459))
    routing_no = str(random.randint(11111111, 88888888))
    date_created = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')
    balance = str(round(random.uniform(1.00, 10000.00),2))
    account_type = random.choice(['CHECKING', 'SAVINGS'])
    status = random.choice(['ACTIVE', 'INACTIVE'])

    val = "(" + "'" + account_no + "'" + "," + "'" + routing_no + "'" + ","  + "'" + date_created + "'" + "," +  balance + "," + "'" + account_type + "'" + "," + "'" + status + "'" + "," + "'" + customer_id + "'" ");"
    print(sql + val)

def card_account_scripts():
    print("card account scripts")

    fake = Faker()

    for i in range(1, 4):

        sql = "INSERT INTO dsbank.card_accounts_by_card_no(card_no,card_name,date_created,card_limit,balance,status,customer_id) " \
              "VALUES "

        card_no = str(random.randint(1000000000000000, 9999999999999999))
        card_name = random.choice(['AMEX', 'VISA', 'MASTERCARD'])
        customer_id = str(random.randint(123456, 123459))
        date_created = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')
        balance = str(round(random.uniform(1.00, 10000.00),2))
        limit = str(round(random.uniform(1.00, 10000.00),2))
        status = random.choice(['ACTIVE', 'INACTIVE'])

        val = "(" + "'" + card_no + "'" + "," + "'" + card_name + "'" + ","  + "'" + date_created + "'" + "," +  limit + "," +  balance +  "," + "'" + status + "'" + "," + "'" + customer_id + "'" ");"
        print(sql + val)

def bank_transaction_scripts():

    fake = Faker()

    for i in range(1, 20):

        sql_transactions = "INSERT INTO dsbank.bank_transactions_by_account_no(account_no,transaction_id,date_time,amount,balance,transaction_type,status,customer_id,account_type) " \
              "VALUES"

        account_no = str(random.randint(1, 10000))
        customer_id = str(random.randint(123456, 123459))
        transaction_id = str(uuid.uuid1())
        date_time = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')

        amount = str(round(random.uniform(1.00, 10000.00),2))
        balance = str(round(random.uniform(1.00, 10000.00),2))

        account_type = random.choice(['CHECKING', 'SAVINGS'])
        transaction_type = ''
        if (account_type in ['SAVINGS']):
            transaction_type = 'TRANSFER'
            plusminus = random.choice(['','-'])
            amount = plusminus + amount

        if (account_type in ['CHECKING']):
            transaction_type = random.choice(['DEPOSIT', 'WITHDRAWL','TRANSFER'])
            if (transaction_type in ['WITHDRAWL']):
                amount = '-' + amount
            if (transaction_type in ['TRANSFER']):
                plusminus = random.choice(['','-'])
                amount = plusminus + amount

        status = random.choice(['PENDING', 'CONFIRMED'])

        val = "(" + "'" + account_no + "'" + "," + transaction_id + "," + "toTimeStamp(" + "'" + date_time + "')" + "," + amount + "," + balance + "," + "'" + transaction_type + "'"+ "," + "'" + status + "'" + "," + "'" + customer_id + "'" +"," + "'" + account_type + "'"");"
        print(sql_transactions + val)

def card_transaction_scripts():

    fake = Faker()

    for i in range(1, 200):

        sql_transactions = "INSERT INTO dsbank.card_transactions_by_card_no(card_no,card_name,transaction_id,date_time,amount,type,status,merchant,category,customer_id) " \
              "VALUES"

        card_no = str(random.randint(1000000000000000, 9999999999999999))
        card_name = random.choice(['AMEX', 'VISA', 'MASTERCARD'])
        customer_id = str(random.randint(123456, 123459))
        transaction_id = str(uuid.uuid1())
        date_time = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2021, 10, 31)).strftime('%Y-%m-%d')

        amount = "-"+str(+round(random.uniform(1.00, 200.00),2))
        type = random.choice(['DEBIT'])
        status = random.choice(['PENDING', 'CONFIRMED'])
        merchant = random.choice(["AMAZON","KROGER","MACYS","COSTCO","TARGET","WALMART","CHICKFILA","HOMEGOODS","MICHAELS","CHIPOTLE","PIZZAHUT","DOMINOS"])
        if (merchant in ["AMAZON"]):
            category = "ECOMMERCE"
        if (merchant in ["COSTCO"]):
            category = "WHOLESALE"
        if (merchant in ["KROGER"]):
            category = "GROCERY"
        if (merchant in ["WALMART","TARGET","HOMEGOODS","MACYS","MICHAELS"]):
            category = "DEPT STORE"
        if (merchant in ["CHIPOTLE","PIZZAHUT","DOMINOS","CHICHFILA"]):
            category = "RESTAURANT"


        val = "(" + "'" + card_no + "'" + "," "'" + card_name + "'" +  "," + transaction_id + "," + "toTimeStamp(" + "'" + date_time + "')" + "," + amount + "," + "'" + type + "'"+ "," + "'" + status + "'" + "," + "'" + merchant + "'" "," + "'" + category + "'" + "," + "'" + customer_id + "'" ");"
        print(sql_transactions + val)


# customer_scripts()

bank_account_scripts()
# card_account_scripts()
# bank_transaction_scripts()
# card_transaction_scripts()



