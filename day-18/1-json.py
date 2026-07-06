import json
product = {
    "name":"Lenovo",
    "price":"72000"
}

# To convert a dictionary to JSON formatted string
print(type(product))
json_data = json.dumps(product)
print(product)
print(json_data)
print(type(json_data))

# convert the JSON formatted string to dictionary.
json_string = '''{
  "user_id": 101,
  "name": "Arjun Sharma",
  "is_active": true,
  "roles": ["admin", "editor"],
  "profile": {
    "location": "Nashik",
    "joined_year": 2026
  },
  "termination_date": null
}'''

data = json.loads(json_string)
print(data)
print(type(data))

# handel json file
products = {
    "product_id": "PROD-83920",
    "name": "NovaSound Pro Wireless Headphones",
    "category": "Electronics",
    "price": 149.99,
    "in_stock": True,
    "tags": ["audio", "bluetooth", "noise-canceling"]
  }

with open('products.json','w') as file:
    json.dump(products,file,indent=4)


with open('products.json','r') as file:
    data = json.load(file)
    print(data)