
from cart_repo import add_item, get_all_items

print("Cart Repository Test Started")

# Test 1 - Add item
result = add_item("Laptop", 50000, 1)

print(result)

# Test 2 - Get all items
items = get_all_items()

print("Cart Items:")

for item in items:
    print(item)

print("Repository Test Completed")

from cart_repo import add_item, get_all_items

print("Cart Repository Test Started")

result = add_item("Mobile", 25000, 1)

print(result)

items = get_all_items()

print("Cart Items:")

for item in items:
    print(item)

print("Repository Test Completed")