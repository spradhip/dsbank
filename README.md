# Summary

The intent of this app is to showcase an app that leverages Streaming, Operational Datastore and API based access for a Dashboard that shows Banking and Credit Card transactions. Astra Streaming (based on Apache Pulsar) and Astra DB (based on Apache Cassandra) and Stargate APIs (stargate.io) and Retool are utilized for the prurposes of this demo. There are two parts to this code base 1) Python code to ingest data to Astra Streaming 2) Retool for UI layer that reads data from Astra DB 3) There is also some setup done to "sink" Astra Streaming to Astra DB

## Components

- DataStax Astra Streaming
- DataStax Astra DB (stores operational data)
- Retool

## Setup Required
```shell
pip install python-dotenv
pip install pulsar-client==2.9.1
pip install faker
pip3 install 'pulsar-client[avro]'
```

## Execution
