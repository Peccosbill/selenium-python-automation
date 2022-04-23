import json

with open("client.json") as client:
    client_dict = json.load(client)
print(client_dict['last articles']['clothes'])

person_dict = {
    "name": "Clark",
    "lastName": "Kent",
    "nickname": "Superman",
    "language": ["Kriptonian", "English"]
}

with open("customer.json", "w") as customer:
    json.dump(person_dict, customer)

with open("customer.json") as customer:
    customer_dict = json.load(customer)
print(customer_dict)
