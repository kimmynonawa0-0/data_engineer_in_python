#using BeautifulSoup
from bs4 import BeautifulSoup
import requests

url3 = 'https://www.python.org/~guido/'
request = requests.get(url3)
r = request.text
soup = BeautifulSoup(r)
soup_pretty = soup.prettify()
print(soup_pretty)

a_tags = soup.find_all('a')
#print(a_tags)
print("the links are:")
for link in a_tags:
    print(link.get('href'))