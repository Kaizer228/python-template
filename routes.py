from flask import Blueprint 

# user controller
from controllers.auth import loginController 
from controllers.auth import getUserController

# here i use our ts structure in mern i ttry to impelement
# luckly gumana hahaha

route = Blueprint('/', __name__)

@route.route('/login/<id>', methods=['POST'])
def login(id):
    return loginController(id)

@route.route('/get-credential/<id>', methods=['GET'])
def getUser(id):
    return getUserController(id)

 