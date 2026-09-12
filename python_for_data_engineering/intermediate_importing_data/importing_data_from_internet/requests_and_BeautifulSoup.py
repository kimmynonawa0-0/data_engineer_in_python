#using BeautifulSoup
from bs4 import BeautifulSoup
import requests

url3 = 'https://www.python.org/~guido/'
request = requests.get(url3) #sending get request
r = request.text #reads the raw html response into a string
soup = BeautifulSoup(r) #instiate object soup that parses the html 
soup_pretty = soup.prettify() #formatting the html text
print(soup_pretty)

a_tags = soup.find_all('a')
#print(a_tags)
print("the links are:")
for link in a_tags:
    print(link.get('href'))