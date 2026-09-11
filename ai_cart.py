import json

# 1. Cart data
cart = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 1
}

# 2. Create message for AI
message = f"""
Product: {cart['name']}
Price: {cart['price']}
Quantity: {cart['quantity']}
"""

print(message)

# 3. Prompt
prompt = message + "\nGive me a simple suggestion about this cart."

print("AI Prompt:")
print(prompt)

# 4. Mock AI response
ai_response = "This is a good laptop choice, but check for a discount before buying."

print("AI Response:")
print(ai_response)


# 5. Function / Tool
def add_item(name, price, quantity):
    total = price * quantity
    return f"{name} added successfully. Total = {total}"


# 6. Agent request
user_request = "Add Laptop and calculate total"

print("User Request:")
print(user_request)


# 7. Agent plan
print("Agent Plan:")

tasks = [
    "Add Laptop",
    "Calculate Total"
]

for task in tasks:
    print("-", task)


# 8. Agent action
print("Agent Actions:")

result = add_item(
    cart["name"],
    cart["price"],
    cart["quantity"]
)

print(result)

total = cart["price"] * cart["quantity"]

print("Cart Total:", total)


# 9. JSON request
request = {
    "action": "add_item",
    "name": cart["name"],
    "price": cart["price"],
    "quantity": cart["quantity"]
}

request_json = json.dumps(request)

print("Agent Request:")
print(request_json)


# 10. JSON parsing
data = json.loads(request_json)

print("Agent Action:", data["action"])
print("Product:", data["name"])
print("Price:", data["price"])
print("Quantity:", data["quantity"])


# 11. Function calling
if data["action"] == "add_item":

    result = add_item(
        data["name"],
        data["price"],
        data["quantity"]
    )

    print("Agent Action Result:")
    print(result)


# 12. Final response
final_message = (
    f"{data['name']} added successfully. "
    f"Your total is ₹{data['price'] * data['quantity']}."
)

print("Agent Final Response:")
print(final_message)