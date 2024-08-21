# POST METHOD
from flask import jsonify, request
from services.products import createProductService, getProductService


def createProductController(id):
    try:
        data = request.get_json()
    
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        response = createProductService(data)
        
        if response.acknowledged:
            return jsonify({"message": "Data inserted successfully" , "response" : str(data)}), 200
     
        return jsonify({"error": "Failed to insert data"}), 500
    
    except Exception as e:
        return jsonify({"error":"error in service creating product", "message" : str(e)}), 500


#GET METHOD
def getProductController(id):
    try:
     if not id:
            return jsonify({"error": "No id provided"}), 400
        
     response = getProductService(id)
     
     if not response:
            return jsonify({"error": "Product not found "}), 400
        
     return jsonify({"response": str(response)}), 200
    
    except Exception as e:
         return jsonify({"error":"error in service fetching product", "message" : str(e)}), 500
    
