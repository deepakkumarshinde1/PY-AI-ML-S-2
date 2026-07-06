import requests
url = 'https://jsonplaceholder.typicode.in/comments'
response = requests.get(url)
print(response.status_code)
data = response.json()

print(len(data))