from flask import Flask, jsonify
from flask_cors import CORS
from getFreeTimes import use

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the route for the root URL
@app.route('/', methods=['GET'])
def home():
    return jsonify(use())

# Run the app only if this file is executed directly
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)