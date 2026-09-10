from cart_repo import (
    add_item,
    get_all_items,
    update_quantity,
    remove_item,
    empty_cart
)


def add_cart_item(name, price, quantity):

    return add_item(name, price, quantity)


def get_cart_items():

    return get_all_items()


def update_cart_item(name, quantity):

    return update_quantity(name, quantity)


def remove_cart_item(name):

    return remove_item(name)


def clear_cart():

    return empty_cart()