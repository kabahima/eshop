from flask import request, jsonify
from api.eshop.models import Products
from api.eshop.utilities import ProductVaildator
from api.database.db import db_handler


#########3 These are to be uncommented later after the setup is done ###


# from api.database.db import db_handler


##########################################################################
products = []

# sellers = []

# users = []

# orders = []


# # function for adding a product
def get_products():
        data = request.get_json()
        product_id = data.get('pdt_id')
        product_name = data.get('pdt_name')
        product_description = data.get('description')
        weight = data.get('weight')
        product_price = data.get('price')
        color = data.get('available_colors')
        # control statement checking the product name , description and price if entered into the database
        if not product_name or not product_description or not product_price:
            return jsonify({ 'status': 400,
                            'error': 'A required field is either missing or empty'
                            })

        products = Products(product_id, product_name, product_description, weight, pdt_name, product_price, color)
        db_lancher().
