# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

#storing the response from get request
response = requests.get(url)
json_data = response.json() #parsing the request into python dictionary
print(json_data)
for key in json_data.keys(): #self explanatory: printing the keys
    print(f"{key}: {json_data[key]}")


