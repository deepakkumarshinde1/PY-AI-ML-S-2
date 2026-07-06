import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
data = response.json()

with open('users.json', 'w') as file:
    json.dump(data,file,indent=4)