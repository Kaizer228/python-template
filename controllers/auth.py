# POST METHOD
from flask import jsonify, request

 
 
# this is the way how to get a params 
# parang normal na function lang
def loginController(id):
    try:
        #like in express req.body 
        data = request.get_json()
        print(id)
        
        #pang deconstruct ng objects
        name, age = data['name'], data['age']

        if not name and age:
            return jsonify({"error": "No data provided"}), 400
        
        return jsonify({"message": "Data received", "name": name, "age": age}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#GET METHOD
def getUserController(id):
    try:
     
     data = {
      "name": "Marc",
      "age": 19,
      "email": "martinezmarc@gmail.com"
     }
     print(id)

     if not data:
            return jsonify({"error": "No data provided"}), 400
        
     return jsonify({"response": data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
