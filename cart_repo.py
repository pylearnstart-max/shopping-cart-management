from db import get_connection


def add_item(name, price, quantity):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO CartItem (name, price, quantity)
        VALUES (?, ?, ?)
    """

    cursor.execute(query, (name, price, quantity))

    connection.commit()
    connection.close()

    return "Item added successfully"
def get_all_items():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT cart_id, name, price, quantity FROM CartItem")

    rows = cursor.fetchall()

    connection.close()

    items = []

    for row in rows:
        items.append({
            "cart_id": row.cart_id,
            "name": row.name,
            "price": float(row.price),
            "quantity": row.quantity
        })

    return items
def update_quantity(name, new_quantity):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE CartItem
        SET quantity = ?
        WHERE name = ?
    """

    cursor.execute(query, (new_quantity, name))

    connection.commit()
    connection.close()

    return "Quantity updated successfully"
def remove_item(name):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM CartItem
        WHERE name = ?
    """

    cursor.execute(query, (name,))

    connection.commit()
    connection.close()

    return "Item removed successfully"
def empty_cart():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM CartItem")

    connection.commit()
    connection.close()

    return "Cart emptied successfully"