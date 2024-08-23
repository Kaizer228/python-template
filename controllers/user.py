# POST METHOD
from flask import jsonify, request
from services.user import registerService, loginService, getUserService
 


def registerController():
    try:
        data = request.get_json()
        # name, age = data.get('name'), data.get('age'), 
        
        if not all(data.get(key) for key in ['name', 'age', 'email', 'password']):
            return jsonify({"message": "Fill all fields"}), 233
       
        response, status_code  = registerService(data)
       
        
        if status_code == 200:
            return jsonify({"message": "Data inserted successfully" , "response" : response}), 200
        if status_code == 234:
            return jsonify({"message": "User already exist" }), 234
     
        return jsonify({f"message": "Failed to insert data"}), 235
        
    
    except Exception as e:
        print(e)
        return jsonify({"message in register controller ": str(e)}), 500

def loginController():
    try:
        data = request.get_json()
        enteredPass = data.get("password")
        if not all(data.get(key) for key in ['email', 'password']):
            return jsonify({"message": "Fill all fields"}), 233
        
        response = loginService(data)
        
        if not response:
           return jsonify({"message": "User not exist"}), 234  
      
        fetchedPass = response.get("password")
        
        if enteredPass != fetchedPass:
         return jsonify({"message": "Wrong password"}), 235
     
        if response and enteredPass == fetchedPass:
         return jsonify({"message": "Succesfully logged", "response" : str(response)}), 200
        
    
    except Exception as e:
        return jsonify({"message in login controller": str(e)}), 500


 
def getUserController(id):
    try:
        
     if not id:
         return jsonify({"response": "no id received"}) , 234
        
     response = getUserService(id)
     
     return response
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
