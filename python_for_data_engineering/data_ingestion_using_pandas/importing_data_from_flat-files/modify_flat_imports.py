import pandas as pd

cols = ['name','address']
data = pd.read_csv('datasets/modify_flat_imports.csv', usecols=cols,nrows= 4)
print(data.head())
print(f"-----------\nrows,columns\n{data.shape}")
print(f"data type of column {data.columns}: {data['name'].dtype}")
print(data.dtypes)