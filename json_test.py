import json

cart = {
    "product": "Laptop",
    "price": 50000,
    "quantity": 1
}

json_data = json.dumps(cart)

print(json_data)