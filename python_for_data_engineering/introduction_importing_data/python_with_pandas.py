import pandas as pd
import kayat as np
from sqlalchemy import create_engine

#TOPIC 1: Reading Data and Inspecting Data
def csv_reader():
    # pd.read_csv() returns a DataFrame – a two‑dimensional table.
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")

    # Inspect the first few rows LIMIT 5
    print(df.head())

    # Check column types and non‑null counts
    print(df.info())

    # See the shape (rows, columns)
    print(df.shape)

def json_reader():
    """this will read the json file"""
    df = pd.read_json(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\second_part\produkto.json")
    print(df.head())
    print(df.info())
    print(df.describe()) #Why it matters: Quickly spot outliers or data quality issues (e.g., negative prices, extreme values) before loading into PostgreSQL.
    
#csv_reader()
#json_reader()
#TOPIC 2: Selecting Columns
def select_columns():
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    print(df['name'])
    selected = df[['name', 'price', 'is_active']]
    print(selected.shape)
    print(df.head())
    print(df)
    select_columns()

# TOPIC 3: Filtering Rows
def filter_rows():
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    filtered = df[(df['price']>100) & (df['category'].str.lower() =='electronics') ]
    filtered_isin = df[(df['category'].str.lower().isin(['furniture','electronics'])) & (df['price'] >=30)]
    filtered_product_mouse = df[(df['name'].str.contains('mouse', case=False)) & (df['price']>20)]
    #print(filtered[['name','price','category']])
    #print(filtered)
    #print(filtered_isin.info())
    print(filtered_product_mouse)
   # print(df.head())
    filter_rows()

# Topic 4: Adding/Transforming Columns
def adding_transforming():
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    #['price_with_tax'] = df['price'] * 1.08
   # df['price_category'] = df['price'].apply(lambda x: 'high' if x>100 else 'low')
    df['price_with_discount'] = df['price'] * 0.9
    df['category_upper'] = df['category'].str.upper()
    print(df[['name','price','price_with_discount','category_upper']].head())
    adding_transforming()
 
# Topic 5: Handling Missing Values
def handling_missing_values():
    data = {
    'name': ['Laptop', 'Mouse', None, 'Keyboard'],
    'price': [1200, 45, 89, None],
    'category': ['Electronics', 'Electronics', None, 'Electronics']
    }
    df = pd.DataFrame(data)
    df_clean = df.dropna()
    df_filled = df.fillna({'name':'Unknown','price': 0,'category': 'Unknown'})
    print(f"nulls:\n{df.isnull().sum()}\nbefore cleaning:\n{df}\nafter cleaning:\n{df_clean}\nbeing filled:\n{df_filled}\ntotal nulls:\n{df_filled.isnull().sum()}")
    handling_missing_values()

# Topic 6: Grouping & Aggregating in Pandas
def grouping_aggregating():
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    print(df)
    grouped = df.groupby('category')['price'].sum()
    grouped_flat = df.groupby('category')['price'].sum().reset_index() # convert to regular table
    # multiple aggregations in the column price
    grouped_aggregate = df.groupby('category')['price'].agg(['sum','mean','count','max','min'])
    # multiple aggregations on different columns
    grouped_multi = df.groupby('category').agg({
        'price': ['sum','count','max','min'],
        'is_active': 'sum'
    })
    print(grouped)
    #print(grouped_aggregate)
    #print(grouped_multi)
    print(grouped_flat) 

    grouping_aggregating()

def practice_task_for_topic_6():
    df = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    grouped = df.groupby('category').agg({
        'price': ['sum','mean'],
        'name': 'count'
    })
    print(grouped.reset_index())
    print("")
    print(grouped)
    practice_task_for_topic_6()

# Topic 7: Merging DataFrames (pd.merge() – like SQL JOIN)
def merging_dataframe():
    df_produkto = pd.read_csv(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv",header=None)
    orders_data = {
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop'],
    'quantity': [2, 5, 1, 3],
    'order_date': ['2025-01-15', '2025-01-18', '2025-01-22', '2025-01-25']
    }
    df_orders = pd.DataFrame(orders_data)
    left_join = pd.merge(df_produkto,df_orders, left_on='name', right_on='product_name',how='left')
    inner_join = pd.merge(df_produkto, df_orders, left_on='name', right_on='product_name', how='inner')
    print(f"produkto:\n{df_produkto.head()}")
    print(f"orders:\n{df_orders.head()}")
    print(f"\ninner join:\n{inner_join}")
    print(f"left join:\n{left_join}")

    merging_dataframe()

 #configs
username = 'postgres'
password = 'hacker123'
hostname = 'localhost'
port = 5432
database = 'postgresql_part1'

def extract_data(filepath):
    """extracting data from csv"""
    return pd.read_csv(filepath)

def transform_data(df):
    """cleaning the extracted data by removing null values"""
    df = df.dropna()
    df['price_with_tax'] = np.round(df['price']*1.08, 2)
    return df
def load_data(df, table_name):
    """loading the data using sqlalchemy"""   
    #create connection string
    connection_string = f"postgresql://{username}:{password}@{hostname}:{port}/{database}"
    engine = create_engine(connection_string)
    df.to_sql(table_name,engine, if_exists='replace', index=False)
    print(f"connection success! {len(df)} rows loaded to {table_name}")
def main():
    raw = extract_data(r"C:\kimchi\data_engineer\postgre_sql\first_mini_ETL_pipeline\produkto.csv")
    clean = transform_data(raw)
    load_data(clean, "produkto_ver2")
if __name__ == "__main__":
    main()

