cart = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 1
}

message = f"""
Product: {cart['name']}
Price: {cart['price']}
Quantity: {cart['quantity']}
"""

print(message)
prompt = message + "\nGive me a simple suggestion about this cart."

print("AI Prompt:")
print(prompt)
ai_response = "This is a good laptop choice, but check for a discount before buying."

print("AI Response:")
print(ai_response)
def add_item(name, price, quantity):
    total = price * quantity
    return f"{name} added successfully. Total = {total}"


result = add_item("Laptop", 50000, 1)

print("Function Result:")
print(result)
def add_item(name, price, quantity):
    total = price * quantity
    return f"{name} added successfully. Total = {total}"


user_request = "Add Laptop to cart"

if "add" in user_request.lower():
    result = add_item("Laptop", 50000, 1)
    print("Function Result:")
    print(result)
user_request = "Add Laptop and calculate total"

print("User Request:")
print(user_request)
user_request = "Add Laptop and calculate total"

print("User Request:")
print(user_request)
print("Agent Plan:")

tasks = [
    "Add Laptop",
    "Calculate Total"
]

for task in tasks:
    print("-", task)
print("Agent Actions:")

result = add_item("Laptop", 50000, 1)
print(result)

total = 50000 * 1
print("Cart Total:", total)
final_response = f"Laptop added successfully. Your cart total is ₹{total}."

print("Agent Final Response:")
print(final_response)
import json

request = {
    "action": "add_item",
    "name": "Laptop",
    "price": 50000,
    "quantity": 1
}

request_json = json.dumps(request)

print("Agent Request:")
print(request_json)
data = json.loads(request_json)

print("Agent Action:", data["action"])
print("Product:", data["name"])
print("Price:", data["price"])
print("Quantity:", data["quantity"])
if data["action"] == "add_item":
    result = add_item(
        data["name"],
        data["price"],
        data["quantity"]
    )

    print("Agent Action Result:")
    print(result)
final_message = (
    f"{data['name']} added successfully. "
    f"Your total is ₹{data['price'] * data['quantity']}."
)

print("Agent Final Response:")
print(final_message)