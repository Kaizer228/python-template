# POST METHOD
from flask import jsonify, request
from config.database import dynamicCollection
from bson.objectid import ObjectId


def registerController():
    try:
        data = request.get_json()
        name, age = data.get('name'), data.get('age')

        if not name or not age:
            return jsonify({"error": "Name and age are required"}), 400
        
        
        # i create a dynamic collection wherein 
        # you dont need to create more collection function
        
        user_collection = dynamicCollection("users")
        result = user_collection.insert_one(data)
        
        if result.acknowledged:
            return jsonify({"message": "Data inserted successfully" , "response" : str(result.inserted_id)}), 200
        else:
            return jsonify({"error": "Failed to insert data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# disregard the id i use it 
# for finding object id
def loginController(id):
    try:
        data = request.get_json()
        
        name, age, email = data['name'], data['age'],data['email']
        if not name and age:
            return jsonify({"error": "No data provided"}), 400
        
        user_collection = dynamicCollection("users")
        result = user_collection.find_one({"email": email})
        
        if result:
            return jsonify({"message": "Data find successfully", "response" : str(result)}), 200
        else:
            return jsonify({"error": "Failed to find data"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


 
def getUserController(id):
    try:
        
     user_collection = dynamicCollection("users")
     #import objectId library to convert to object is like this
     # format ObjectId('66c4abdafc294beef4cbb760')
     result = user_collection.find_one({"_id": ObjectId(id)})
     print(result)
        
     if not result:
            return jsonify({"error": "User not found "}), 400
        
     return jsonify({"response": str(result)}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
