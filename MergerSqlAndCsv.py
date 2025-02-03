import pandas as pd
from sqlalchemy import create_engine
username = 'root'
password = 'cvr123'
host = 'localhost'
database = 'aimlds'
table_name = 'customer'

connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'


engine = create_engine(connection_string)

df_sql = pd.read_sql(f'SELECT * FROM {table_name}', engine)

csv_file = 'customer_data1.csv'
df_csv = pd.read_csv(csv_file)

df_merged = pd.merge(df_sql, df_csv, on='cnum', how='inner')

df_merged.to_sql(name='merged_customer', con=engine, if_exists='replace', index=False)
df_merged.to_csv('merged_customer_data.csv', index=False)
print(df_merged)
print("Data merged successfully and saved!")
