from flask import Flask, jsonify, render_template
from flask_cors import CORS
from getFreeTimes import use

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the route for the root URL
@app.route('/api', methods=['GET'])
def api():
    return jsonify(use())

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Run the app only if this file is executed directly
if __name__ == '__main__':
    app.run()