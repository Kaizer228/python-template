# POST METHOD
from flask import jsonify, request
from config.database import dynamicCollection
from bson.objectid import ObjectId


def createProduct(id):
    try:
        
        data = request.get_json()
        name, price = data['name'], data['price']

        if not name and price:
            return jsonify({"error": "No data provided"}), 400
        
        product_collection = dynamicCollection("users")
        result = product_collection.insert_one(data)
        
        if result.acknowledged:
            return jsonify({"message": "Data inserted successfully" , "response" : str(result.inserted_id)}), 200
        else:
            return jsonify({"error": "Failed to insert data"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#GET METHOD
def getProducts(id):
    try:
     product_collection = dynamicCollection("users")
     result = product_collection.find_one({"_id": ObjectId(id)})
    
     if not result:
            return jsonify({"error": "No data provided"}), 400
        
     return jsonify({"response": str(result)}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
