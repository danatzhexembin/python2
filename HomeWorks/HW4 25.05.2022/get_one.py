import json
import requests

# url = "https://api.instantwebtools.net/v1/airlines/-10"
# response = requests.get(url)
# # Http - ответ. content - данные, статус код - статус запроса
# print(response.status_code)
# json_data = response.content.decode()
# print(type(json_data))

url = "https://api.instantwebtools.net/v1/airlines/10"
# url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)

url_all = "https://api.instantwebtools.net/v1/airlines"
response_all = requests.get(url_all)
content_all = response_all.content
json_data_all = content_all.decode()
airlines = json.loads(json_data_all)

for airline in airlines:
    with open(f'data_{airline["id"]}', 'w') as file:  # alias - псевдоним
        json.dump(airline, file)
