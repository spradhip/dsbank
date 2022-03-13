from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd


cloud_config= {
        'secure_connect_bundle': 'secure-connect-dsbank.zip'
}
auth_provider = PlainTextAuthProvider('ShqdPBFEwzZEceNeYHutBUew', 's6-ml8tr4I2WXM375qIm.hUJ+A8KsR3x_4ZTOTP1zO8h88wP8DYlvqqAfXToO1yJbMi.z3X3yZX+89yaScoZ,P78DL7zK_Im+DMdfhZ4qvQhnKCH4Z7kn.uOuyeZ0Pe4')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")


# run the CQL query and get the data
result_set = session.execute("select * from dsbank.bank_transactions_by_account_no limit 1000;")

df1 = pd.DataFrame(result_set.column_names)
print(df1)

df2 = pd.DataFrame(result_set._current_rows)
print(df2)