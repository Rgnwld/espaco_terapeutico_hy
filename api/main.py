from flask import Flask, jsonify, request
from routes.user import initDb
from db_connection import test_connection
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

if __name__ == '__main__':
    @app.route('/api', methods=['GET'])
    def api():
        return jsonify({"message": "Hello, World!"})
    
    # @app.route('/api/init', methods=['GET'])
    # def teste():
    #     initDb()
        
    @app.route('/api/test')
    def teste():
        return test_connection()

    @app.route('/api/user', methods=['GET'])
    def user():
        initDb()

    @app.route('/api/data', methods=['POST'])
    def data():
        data = request.json
        return jsonify({"received": data}), 201

    app.run(debug=True)