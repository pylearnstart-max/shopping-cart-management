
# Shopping Cart Management System
# Sprint 2 - Remove Item and Empty Cart
# Sprint 3 - Input Validation and Final Testing

cart = []

# =========================
# SPRINT 1
# =========================

# 1. Add Item
def add_item(name, price, quantity):

    if name == "":
        print("Item name cannot be empty")
        return

    if price <= 0:
        print("Price must be greater than 0")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0")
        return

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)
    print("Item added successfully")


# 2. View Cart
def view_cart():

    print("\nShopping Cart:")

    if not cart:
        print("Cart is empty")
        return

    for item in cart:
        print(
            item["name"],
            "- Price:", item["price"],
            "- Quantity:", item["quantity"]
        )


# 3. Update Quantity
def update_quantity(name, new_quantity):

    if new_quantity <= 0:
        print("Quantity must be greater than 0")
        return

    for item in cart:

        if item["name"] == name:
            item["quantity"] = new_quantity
            print("Quantity updated successfully")
            return

    print("Item not found")


# 4. Calculate Total
def calculate_total():

    total = 0

    for item in cart:
        total = total + (item["price"] * item["quantity"])

    print("Total:", total)


# =========================
# SPRINT 2
# =========================

# 5. Remove Item
def remove_item(name):

    for item in cart:

        if item["name"] == name:
            cart.remove(item)
            print("Item removed successfully")
            return

    print("Item not found")


# 6. Empty Cart
def empty_cart():

    cart.clear()
    print("Cart emptied successfully")


# =========================
# SPRINT 1 TESTING
# =========================

print("\n--- Sprint 1 Testing ---")

add_item("Laptop", 50000, 1)
add_item("Mouse", 1000, 2)

view_cart()

update_quantity("Laptop", 2)

view_cart()

calculate_total()


# =========================
# SPRINT 2 TESTING
# =========================

print("\n--- Sprint 2 Testing ---")

remove_item("Mouse")

view_cart()

empty_cart()

view_cart()


# =========================
# SPRINT 3 TESTING
# =========================

print("\n--- Sprint 3 Testing ---")

# Invalid item name
add_item("", 50000, 1)

# Invalid price
add_item("Keyboard", -1000, 1)

# Invalid quantity
add_item("Monitor", 10000, 0)

# Valid item
add_item("Keyboard", 2000, 1)

# Invalid update quantity
update_quantity("Keyboard", 0)

# Item not found
remove_item("Mobile")

view_cart()

calculate_total()
def show_total():
    total = 0

    for item in cart:
        total = total + (item["price"] * item["quantity"])

    print("Cart Total:", total)

def show_item_count():

    count = len(cart)

    print("Number of Items:", count)


show_item_count()