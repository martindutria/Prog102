from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


# Testing Route
@app.route('/')
def index():
    return '<h1>FlASK REST API TEST<h1>'


# Get Data Routes
@app.route('/products')
def get_products():
    # return jsonify(products)
    return jsonify({'products': products})


@app.route('/products/<string:product_name>')
def get_product(product_name):
    products_found = [
        product for product in products if product['name'] == product_name.lower()]
    if len(products_found) > 0:
        return jsonify({'product': products_found})
    return jsonify({'message': 'Product Not found'})


# Create Data Routes
@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        'ecommerce': request.json['ecommerce'],
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'products': products})


# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if len(products_found) > 0:
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': products_found[0]
        })
    return jsonify({'message': 'Product Not found'})


# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if len(products_found) > 0:
        products.remove(products_found)
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })


if __name__ == '__main__':
    app.run(debug=True)
