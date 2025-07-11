from flask import Blueprint, request, jsonify
from app.models.product import Product, db
from app.extensions import bcrypt, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK,HTTP_403_FORBIDDEN


# Create a  service blueprint
products = Blueprint('product', __name__, url_prefix='/api/v1/products')

# Define and  create product endpoint
@products.route('/create', methods=["POST"])
@jwt_required()
def create_product():
    try:
        # Extract product data from the request JSON
        data = request.json
        name = data.get("name")
        quantity = data.get("quantity")
        order_id = data.get("order_id")
        service_id = data.get("service_id")
       

        # Validating data to avoid data redandancy
        if not name or not quantity or not order_id or not service_id:
            return jsonify({'error': "All fields are required"}), HTTP_400_BAD_REQUEST

        # Check if product name already exists
        if Product.query.filter_by(name=name).first() is not None:
            return jsonify({'error': 'product name already exists'}), HTTP_400_BAD_REQUEST

        # Creating a new product 
        new_product = Product(
            name=name,
            quantity=quantity
          
        )

        # Adding the new product instance to the database session
        db.session.add(new_product)
        db.session.commit()

        # Return a success response with the newly created product details
        return jsonify({
            'message':  name + " has been created successfully",
            'product': {
                'id': new_product.product_id,
                'name': new_product.name,
                'quantity': new_product.quantity
         
            
            }
        }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR