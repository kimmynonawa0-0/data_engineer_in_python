import pandas as pd
data = {
    'ride_id': [101, 102, 103, 104, 105],
    'user_type': [1, 2, 3, 1, 2],               
    'duration': ['15 minutes', '22 minutes', '30 minutes', '10 minutes', '45 minutes'], 
    'start_station': ['A', 'B', 'C', 'A', 'B'],
    'end_station': ['B', 'C', 'D', 'B', 'C']
}

df = pd.DataFrame(data)
print(df.head(2))
print(df.info())
print(df.describe())

df['user_type_cat'] = df['user_type'].astype('category')
try:
    assert df['user_type_cat'].dtype == 'category'
except AssertionError:
    print("wrong datatype!")
df['duration_trim'] = df['duration'].str.strip('minutes')
df['duration_trim_int'] = df['duration_trim'].astype('int')
try:
    assert df['duration_trim_int'].dtype == 'int'
except AssertionError:
    print("wrong data type!")
    
print("--------------------------")
print(df.head(2))
print(df.info())
print(df.describe())
print(df['duration_trim_int'].mean())