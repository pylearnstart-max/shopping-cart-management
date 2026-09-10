from flask import Flask, request, jsonify
from cart_service import (
    add_cart_item,
    get_cart_items,
    update_cart_item,
    remove_cart_item,
    clear_cart
)

app = Flask(__name__)


@app.route("/")
def home():
    return "Shopping Cart API is running"


@app.route("/cart", methods=["GET"])
def get_cart():

    items = get_cart_items()

    return jsonify(items)


@app.route("/cart", methods=["POST"])
def create_cart_item():

    data = request.get_json()

    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    result = add_cart_item(name, price, quantity)

    return jsonify({
        "message": result
    }), 201


@app.route("/cart/<name>", methods=["PUT"])
def update_cart_item_api(name):

    data = request.get_json()

    quantity = data["quantity"]

    result = update_cart_item(name, quantity)

    return jsonify({
        "message": result
    })


@app.route("/cart/<name>", methods=["DELETE"])
def delete_cart_item(name):

    result = remove_cart_item(name)

    return jsonify({
        "message": result
    })


@app.route("/cart", methods=["DELETE"])
def clear_cart_api():

    result = clear_cart()

    return jsonify({
        "message": result
    })


if __name__ == "__main__":
    app.run(debug=True)