
CREATE KEYSPACE IF NOT EXISTS dsbank WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

DROP TABLE user_profile_by_user_id;
DROP TABLE customer_profile_by_customer_id;

DROP TABLE bank_accounts_by_account_no;
DROP TABLE bank_transactions_by_account_no;

DROP TABLE card_accounts_by_card_no;
DROP TABLE card_transactions_by_card_no;

DROP TABLE card_summary_by_category_by_month_by_card_no;
DROP TABLE account_summary_by_transaction_type_by_month_by_account_no;


CREATE TABLE customer_profile_by_customer_id(
    customer_id text,
    first_name text,
    last_name text,
    dob date,
    gender text,
    email text,
    phone_no text,
    address1 text,
    address2 text,
    city text,
    state text,
    zip text,
    country text,
    status text,
    status_description text,
    PRIMARY KEY (customer_id)
);

CREATE TABLE user_profile_by_user_id (
    user_id text,
    email text,
    password text,
    customer_id text,
    PRIMARY KEY (user_id)
);

CREATE TABLE bank_accounts_by_account_no(
    account_no text,
    routing_no text,
    account_name text,
    account_nick_name text,
    date_created date,
    balance float,
    account_type text,
    customer_id text,
    status text,
    status_description text,    
    account_type_description text,    
    PRIMARY KEY (account_no)
);

CREATE TABLE bank_transactions_by_account_no(
   account_no text,
   account_type text,
   transaction_id uuid,
   date_time timestamp,
   amount decimal,
   balance decimal,
   external_account_number text,
   external_account_name text,
   description text,
   status text,
   transaction_type text,
   customer_id text,   
   PRIMARY KEY ((account_no), date_time, transaction_id)
) WITH CLUSTERING ORDER BY (date_time DESC, transaction_id DESC);


CREATE TABLE card_accounts_by_card_no(
    card_no text,
    card_name text,
    account_name text,
    account_nick_name text,
    date_created date,
    balance decimal,
    card_limit decimal,
    account_type text,
    expiry_date date,
    bank_account_no text,
    customer_id text,
    status text,
    PRIMARY KEY (card_no)
);

CREATE TABLE card_transactions_by_card_no(
   card_no text,
   card_name text,
   transaction_id uuid,
   date_time timestamp,
   amount decimal,
   merchant text,
   description text,
   location text,
   status text,
   type text,
   category text,   
   customer_id text,   
   PRIMARY KEY ((card_no), date_time, transaction_id)
) WITH CLUSTERING ORDER BY (date_time DESC, transaction_id DESC);

-- not sure if this table below is required
CREATE TABLE card_summary_by_category_by_month_by_card_no(
    account_no int,
    date_time timestamp,
    category text,
    amount decimal,
    customer_id text,
    PRIMARY KEY ((account_no, date_time), category)
) WITH CLUSTERING ORDER BY (category ASC);

-- not sure if this table below is required
CREATE TABLE account_summary_by_transaction_type_by_month_by_account_no(
    account_no int,
    date_time timestamp,
    type text,
    amount decimal,
    customer_id text,
    PRIMARY KEY ((account_no, date_time), transaction_type)
) WITH CLUSTERING ORDER BY (transaction_type ASC);