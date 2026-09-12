import pandas as pd

data = 'datasets/winequality-red.csv'
df_first100 = pd.read_csv(data, nrows=100)
df_next50 = pd.read_csv(data,
                 skiprows=100,
                 nrows=50,
                 header=None,
                 names=list(df_first100))
print(df_first100.head())
print(df_next50.head())