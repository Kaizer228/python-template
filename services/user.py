from flask import jsonify
from config.database import dynamicCollection
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

def registerService(data):
     try:
       user_collection = dynamicCollection("users")
       result = user_collection.insert_one(data)
       return str(result) , 200
     
     #this is a built in func of pymongo to
     # receive if value is unique try/catch
     except DuplicateKeyError:
      return jsonify({"error": "User already exist"}), 234

     
     
def loginService(data):
  try:
    
     email = data["email"]
     user_collection = dynamicCollection("users")
     result = user_collection.find_one({"email": email})
        
     return result
    
  except : 
        return jsonify({"error": "Failed to log-in"}), 500
        
     
       
       
def getUserService(id):
     
     user_collection = dynamicCollection("users")
     #import objectId library to convert to object is like this
     # format ObjectId('66c4abdafc294beef4cbb760')
     result = user_collection.find_one({"_id": ObjectId(id)})
     print(result)
        
     if not result:
            return jsonify({"error": "User not found "}), 400
        
     return jsonify({"response": str(result)}), 200
 
   