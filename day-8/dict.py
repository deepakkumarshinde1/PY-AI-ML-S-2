# dict
# set key value pair
# are mutable in nature

set1 = {"Deepak",21,"Yes",55.50}
studentDetails = {
        "name":"Deepak",
        "age":21,
        "isPresent": "Yes",
        "marks": 55.50
    }
#print(type(set1)) # set
#print(type(studentDetails)) #dict

product = dict(name="dell",price=42000)
# print(product)

product = {
    "name":"lenovo",
    "price":42000
}

# read
#print(product['name']) # value
# If a key is not available, square bracket will generate a error.

#print(product.get('name')) # value
# If the key is not available, gate will return none.

for key in product:
    # print(key)
    pass

for value in product.values():
    # print(value)
    pass

for key,value in product.items():
    # print(key,value)
    pass


product = {
    "name":"lenovo",
    "price":42000
}

# add
product['location'] = "Nashik"

# remove
# product.pop('price')
del product['name']
# product.clear()
print(product)

# check
isThere = "name" in product
print(isThere)

product2 = product.copy()
print(product2)

# nested dict
student = {
    "s1":{
        "name":"deepak",
        "age":36
    },
    "s2":{
        "name":"om",
        "age":21
    }
}

student["s1"]["name"]
student["s1"]["age"]

for key,value in student.items():
    for c_key,c_value in value.items():
        print(f"student {key} has {c_key} ={c_value}")