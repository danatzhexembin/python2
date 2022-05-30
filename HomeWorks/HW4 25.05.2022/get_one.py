import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)
