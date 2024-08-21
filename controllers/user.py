# POST METHOD
from flask import jsonify, request
from services.user import registerService, loginService, getUserService
 


def registerController():
    try:
        data = request.get_json()
        name, age = data.get('name'), data.get('age')

        if not name or not age:
            return jsonify({"error": "Name and age are required"}), 400
        
        
        response, status_code  = registerService(data)
        print(response)
        
        if status_code == 200:
            return jsonify({"message": "Data inserted successfully" , "response" : response}), 200
        if status_code == 234:
            return jsonify({"message": "User already exist" }), 234
     
        return jsonify({f"error": "Failed to insert data"}), 500
        
    
    except Exception as e:
        return jsonify({"error in register controller ": str(e)}), 500

# disregard the id i use it 
# for finding object id
def loginController(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        response = loginService(data)
        return response
    
    except Exception as e:
        return jsonify({"error in login controller": str(e)}), 500


 
def getUserController(id):
    try:
        
     if not id:
         return jsonify({"response": "no id received"}) , 234
        
     response = getUserService(id)
     
     return response
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
