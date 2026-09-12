import numpy as np
import pandas as pd
data = np.genfromtxt(r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\flat_files\datasets\flat.csv", delimiter=',')
print(f"{data}\n")
print(data[1][1])

df = pd.read_csv(r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\flat_files\datasets\flat.csv")
print(df.head().reset_index())
print(f"\n{df.head()}\n")

#pwd kita mag import pira la ka rows saton datafame using nrows=
df2 = pd.read_csv(r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\flat_files\datasets\number_of_rows.csv",nrows=4)
print(f"{df2.head()}\n")

#i loaded the excel file xlsx to a DataFrame
data = r"C:\kimchi\data_engineer\python\python_topics\software_engineering\data_egineer_in_python\introduction_importing_data\flat_files\datasets\excel_proj.xlsx"
df = pd.read_excel(data,nrows=5)
print(df)