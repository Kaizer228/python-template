# POST METHOD
from flask import jsonify, request


def createProduct(id):
    try:
        
        data = request.get_json()
        print(id)
        
        name, price = data['name'], data['price']

        if not name and price:
            return jsonify({"error": "No data provided"}), 400
        
        return jsonify({"message": "Data received", "name": name, "age": price}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#GET METHOD
def getProducts(id):
    try:
     
     data = {
      "name": "Malungay",
      "price": 193,
      
     }
     print(id)

     if not data:
            return jsonify({"error": "No data provided"}), 400
        
     return jsonify({"response": data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
