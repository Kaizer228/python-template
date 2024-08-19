from flask import Blueprint 

# user controller
from controllers.user import loginController 
from controllers.user import getUserController

# product controller
from controllers.product import createProduct
from controllers.product import getProducts
# here i use our ts structure in mern i ttry to impelement
# luckly gumana hahaha

route = Blueprint('/', __name__)

@route.route('/login/<id>', methods=['POST'])
def login(id):
    return loginController(id)

@route.route('/get-credential/<id>', methods=['GET'])
def getUser(id):
    return getUserController(id)

@route.route('/create-product/<id>', methods=['POST'])
def product(id):
    return createProduct(id)

@route.route('/get-products/<id>', methods=['GET'])
def getProducts(id):
    return getProducts(id)

 
 
 
 