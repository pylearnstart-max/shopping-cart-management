# Shopping Cart Management System
# Sprint 1 - Basic Cart Operations
# Sprint 2 - Remove Item and Empty Cart
# Sprint 3 - Input Validation
# Sprint 4 - Search, Discount, Item Count and Menu

cart = []


# =========================
# 1. ADD ITEM
# =========================

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


# =========================
# 2. VIEW CART
# =========================

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


# =========================
# 3. UPDATE QUANTITY
# =========================

def update_quantity(name, new_quantity):

    if new_quantity <= 0:
        print("Quantity must be greater than 0")
        return

    for item in cart:

        if item["name"].lower() == name.lower():
            item["quantity"] = new_quantity
            print("Quantity updated successfully")
            return

    print("Item not found")


# =========================
# 4. CALCULATE TOTAL
# =========================

def calculate_total():

    total = 0

    for item in cart:
        total = total + (
            item["price"] * item["quantity"]
        )

    print("Total:", total)

    return total


# =========================
# 5. REMOVE ITEM
# =========================

def remove_item(name):

    for item in cart:

        if item["name"].lower() == name.lower():
            cart.remove(item)
            print("Item removed successfully")
            return

    print("Item not found")


# =========================
# 6. EMPTY CART
# =========================

def empty_cart():

    cart.clear()
    print("Cart emptied successfully")


# =========================
# 7. SHOW TOTAL
# =========================

def show_total():

    total = 0

    for item in cart:
        total = total + (
            item["price"] * item["quantity"]
        )

    print("Cart Total:", total)


# =========================
# 8. SHOW ITEM COUNT
# =========================

def show_item_count():

    count = len(cart)

    print("Total Items Count:", count)


# =========================
# 9. APPLY DISCOUNT
# =========================

def apply_discount(discount_percent):

    if discount_percent < 0 or discount_percent > 100:
        print("Discount must be between 0 and 100")
        return

    total = 0

    for item in cart:
        total = total + (
            item["price"] * item["quantity"]
        )

    discount = total * discount_percent / 100
    final_total = total - discount

    print("Original Total:", total)
    print("Discount:", discount)
    print("Final Total:", final_total)


# =========================
# 10. SEARCH ITEM
# =========================

def search_item(name):

    for item in cart:

        if item["name"].lower() == name.lower():

            print(
                item["name"],
                "- Price:", item["price"],
                "- Quantity:", item["quantity"]
            )

            return

    print("Item not found")


# =========================
# MANUAL TESTING
# =========================

def manual_testing():

    print("\n--- Sprint Testing ---")

    add_item("Laptop", 50000, 1)
    add_item("Mouse", 1000, 2)

    view_cart()

    update_quantity("Laptop", 2)

    view_cart()

    calculate_total()

    remove_item("Mouse")

    view_cart()

    add_item("", 50000, 1)
    add_item("Keyboard", -1000, 1)
    add_item("Monitor", 10000, 0)

    add_item("Keyboard", 2000, 1)

    search_item("keyboard")

    show_item_count()

    apply_discount(10)


# =========================
# SPRINT 4 - MENU
# =========================

def menu():

    while True:

        print("\n===== SHOPPING CART =====")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Search Item")
        print("6. Calculate Total")
        print("7. Apply Discount")
        print("8. Show Item Count")
        print("9. Empty Cart")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                name = input("Enter item name: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))

                add_item(name, price, quantity)

            except ValueError:
                print("Invalid price or quantity")


        elif choice == "2":

            view_cart()


        elif choice == "3":

            try:
                name = input("Enter item name: ")
                quantity = int(input("Enter new quantity: "))

                update_quantity(name, quantity)

            except ValueError:
                print("Invalid quantity")


        elif choice == "4":

            name = input("Enter item name: ")

            remove_item(name)


        elif choice == "5":

            name = input("Enter item name: ")

            search_item(name)


        elif choice == "6":

            calculate_total()


        elif choice == "7":

            try:
                discount = float(
                    input("Enter discount percentage: ")
                )

                apply_discount(discount)

            except ValueError:
                print("Invalid discount")


        elif choice == "8":

            show_item_count()


        elif choice == "9":

            empty_cart()


        elif choice == "10":

            print("Thank you for using Shopping Cart!")
            break


        else:

            print("Invalid choice")


# =========================
# PROGRAM START
# =========================

if __name__ == "__main__":

    # Uncomment this line only when you want manual testing.
    # manual_testing()

    menu()