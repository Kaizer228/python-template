# POST METHOD
from flask import jsonify, request
from services.user import registerService, loginService, getUserService
 


def registerController():
    try:
        data = request.get_json()
        # name, age = data.get('name'), data.get('age'), 
        
        if not all(data.get(key) for key in ['name', 'age', 'email', 'password']):
            return jsonify({"message": "Fill all fields", "status" : 404}), 404
       
        response, status_code  = registerService(data)
       
        
        if status_code == 200:
            return jsonify({"message": "Data inserted successfully" , "response" : response, 
            "status" : status_code}), 200
        if status_code == 234:
            return jsonify({"message": "User already exist",
             "status" : status_code}), 234
     
        return jsonify({f"message": "Failed to insert data",
             "status" : status_code}), 500
        
    
    except Exception as e:
        print(e)
        return jsonify({"message in register controller ": str(e)}), 500

def loginController():
    try:
        data = request.get_json()
        enteredPass = data.get("password")
        if not all(data.get(key) for key in ['email', 'password']):
            return jsonify({"message": "Fill all fields", "status" : 404}), 404
        
        response = loginService(data)
        
        if not response:
           return jsonify({"message": "User not exist" , "status" : 234}), 234  
      
        fetchedPass = response.get("password")
        
        if enteredPass != fetchedPass:
         return jsonify({"message": "Wrong password",  "status" : 400}), 400
     
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
    
