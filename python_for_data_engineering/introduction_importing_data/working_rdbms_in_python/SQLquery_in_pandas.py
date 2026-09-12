from sqlalchemy import create_engine, text
import pandas as pd

hostname = 'localhost'
username = 'postgres'
db_name = 'erp'
port_id = 5432
pwd = 'hacker123'

#u must create an engine
engine = create_engine(f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{db_name}")

df = pd.read_sql_query('SELECT * FROM h;', engine)
print(df.head())