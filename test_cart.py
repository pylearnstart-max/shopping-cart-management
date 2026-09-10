import cart

print("Shopping Cart Test Started")

cart.cart.clear()

cart.add_item("Laptop", 50000, 1)

assert len(cart.cart) == 1
assert cart.cart[0]["name"] == "Laptop"
assert cart.cart[0]["price"] == 50000
assert cart.cart[0]["quantity"] == 1

print("Test 1 passed")

cart.add_item("Mouse", 1000, 2)

assert len(cart.cart) == 2

print("Test 2 passed")

cart.update_quantity("Laptop", 2)

assert cart.cart[0]["quantity"] == 2

print("Test 3 passed")

total = cart.calculate_total()

assert total == 102000

print("Test 4 passed")

cart.search_item("Mouse")

print("Test 5 passed")

cart.remove_item("Mouse")

assert len(cart.cart) == 1

print("Test 6 passed")

cart.apply_discount(10)

print("Test 7 passed")

cart.show_item_count()

assert len(cart.cart) == 1

print("Test 8 passed")

cart.empty_cart()

assert len(cart.cart) == 0

print("Test 9 passed")

print("All Shopping Cart Tests Passed")