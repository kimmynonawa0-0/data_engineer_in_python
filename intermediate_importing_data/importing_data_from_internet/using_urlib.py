from urllib.request import urlretrieve
import pandas as pd



url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, 'winequality-red.csv') #this saves the file locally (ikaw mag buot nano name san file)
df = pd.read_csv('winequality-red.csv', delimiter=";")
print(df.head())



#method 2
url2 = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
df2 = pd.read_csv(url2, delimiter=";") #you can directly read a file from the web without downloading it
print(df2.head())










