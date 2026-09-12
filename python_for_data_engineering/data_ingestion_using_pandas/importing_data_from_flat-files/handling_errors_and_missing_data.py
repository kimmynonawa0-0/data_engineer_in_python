import pandas as pd
"""data = 'datasets/modify_flat_imports.csv'
data_types = {'name':'category',
              'address':'category'}
df = pd.read_csv(data, dtype=data_types)
print(df.dtypes)

#change the name to str
df['name'] = df['name'].astype(str)
print(f"new data type of column {df.columns[0]}: {df['name'].dtype}")"""

data2 = 'datasets/erros_missing_data.csv'
df2 = pd.read_csv(data2)
print(f"bad data:\n{df2.head()}")

na_dict = {'age':[-1,0],
           'income':0,
           'zipcode':0,
           'dependents':-1}
df2 = pd.read_csv(data2, na_values=na_dict)
print(f"handled data:\n{df2.head()}")
print(f"number of None values for column {df2['age'].name}:\n{df2['age'].head().isna()}")
