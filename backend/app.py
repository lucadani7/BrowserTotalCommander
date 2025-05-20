from flask import Flask
from flask_cors import CORS

from backend.routes.file_routes import file_routes

app = Flask(__name__)
CORS(app)  # allowing API access from frontend


@app.route('/')
def home():
    return "Backend is running!"


app.register_blueprint(file_routes)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
