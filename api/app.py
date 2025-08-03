from app import create_app
from flask_cors import CORS
import traceback

try:
    app = create_app()
    CORS(app, origins=["http://localhost:3000"])
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    @app.route('/')
    def index():
        return "Welcome to the API!"
    
    if __name__ == '__main__':
        app.run(debug=True, port=5000)
except:
    with open("exceptions.log", "a") as logfile:
        traceback.print_exc(file=logfile)
    raise


