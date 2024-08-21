from flask import jsonify
from config.database import dynamicCollection
from bson.objectid import ObjectId


def createProductService(data):
    
    try:
       name, price = data['name'], data['price']
       if not name and price:
            return jsonify({"error": "No data provided"}), 400
        
       product_collection = dynamicCollection("products")
       result = product_collection.insert_one(data)
       
       return result
   
    except Exception as e :
      return jsonify({f"error": "Error in register service", "message" : str(e)}), 500
     
     
def getProductService(id):
    try:
     product_collection = dynamicCollection("products")
     #import objectId library to convert to object is like this
     # format ObjectId('66c4abdafc294beef4cbb760')
     result = product_collection.find_one({"_id": ObjectId(id)})
    
     return result
 
    except Exception as e:
       return jsonify({f"error": "Error in logging service", "message" : str(e)}), 500
       
       
 