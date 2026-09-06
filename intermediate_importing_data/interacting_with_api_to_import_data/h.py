import requests
import json

#send get request to the api endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts")
json_data = response.json() #parses the the response into python objects(in this case list of dictionaries)
print("---------------------\nusing requests:  ") #if you have to download using api
print(f"total post {len(json_data)}\n")
for p in json_data: #iterating through the list of dictionary
    print(f"userId: {p['userId']} title: {p['title']}")

print(f"\n-------------------------------\nusing context manager:")#if the json file is stored in your files
with open("datasets/movies.json","r") as file:
    data = json.load(file)

for k in data.keys():
    print(f"{k}: {data[k]}")