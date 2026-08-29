import numpy as np
import pandas as pd
file = 'flat.csv'
data = np.genfromtxt(file, delimiter=',')
print(f"{data}\n")
print(data[1][1])

df = pd.read_csv(r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\flat.csv")
print(df.head().reset_index())
print(f"\n{df.head()}\n")

#pwd kit mag import pira la ka rows saton datafame using nrows=
df2 = pd.read_csv(r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\number_of_rows.csv",nrows=4)
print(df2.head())
