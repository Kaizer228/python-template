from flask import Blueprint 

 
from controllers.user import  getUserController , loginController, registerController
from controllers.product import createProductController , getProductController
 
 

route = Blueprint('/', __name__)

@route.route('/register', methods=['POST'])
def registerHandler():
    return registerController()

@route.route('/login/<id>', methods=['POST'])
def loginHandler(id):
    return loginController(id)

@route.route('/get-credential/<id>', methods=['GET'])
def getUserHandler(id):
    return getUserController(id)

@route.route('/create-product/<id>', methods=['POST'])
def productHandler(id):
    return createProductController(id)

@route.route('/get-products/<id>', methods=['GET'])
def getProductsHandler(id):
    return getProductController(id)

 
 
 
 