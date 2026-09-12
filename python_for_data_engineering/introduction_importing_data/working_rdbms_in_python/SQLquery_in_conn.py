from sqlalchemy import create_engine, text
import pandas as pd

hostname = 'localhost'
username = 'postgres'
db_name = 'erp'
port_id = 5432
pwd = 'hacker123'

#u must create an engine
engine = create_engine(f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{db_name}")

#theres no need to create cursor
with engine.connect() as conn:
    print("connection successful!")

    # Show current data 
    result = conn.execute(text("SELECT * FROM h;")) #u must explicit text() 
    print("before insert:", result.fetchall())

    # Insert with ON CONFLICT (DO NOTHING)
    name = 'shai'
    conn.execute(
        text("INSERT INTO h(name) VALUES(:name) ON CONFLICT (name) DO NOTHING;"),
        {"name": name} #dictionary instead of tuple in psycopg2
    )
    conn.commit()

    # Show updated data
    result = conn.execute(text("SELECT * FROM h;"))

   

    #  Fetch again for DataFrame
    result = conn.execute(text("SELECT * FROM h;"))
    df = pd.DataFrame(result.fetchall()) #u can assign the query result
    #df.columns = result.keys()
    print("\nDataFrame:")
    print(df.head())