from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

#routes
from routes import route

 #like in express app.use
app = Flask(__name__)
CORS(app)

app.register_blueprint(route)

 
if __name__ == '__main__':
    app.run(debug=True)


 
    
    