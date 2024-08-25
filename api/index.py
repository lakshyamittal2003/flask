from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/bfhl": {"origins": "*"}})

# User information (hardcoded for now)
user_info = {
    "user_id": "Lakshya_mital",
    "email": "lakshya.mittal2021@vitstudent.ac.in",
    "roll_number": "21BIT0076"
}

# Helper function to categorize data
def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = None
    
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower() and (highest_lowercase is None or item > highest_lowercase):
                highest_lowercase = item

    return numbers, alphabets, highest_lowercase

# POST endpoint
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Get JSON data from request
        req_data = request.json
        data = req_data.get('data', [])
        
        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input data"}), 400
        
        # Process data
        numbers, alphabets, highest_lowercase = process_data(data)

        # Build the response
        response = {
            "is_success": True,
            **user_info,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

# GET endpoint
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
