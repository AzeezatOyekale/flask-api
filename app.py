from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

def get_number_properties(num):
    """Determine properties of the number."""
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 != 0 else "even")
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number')
        if number is None or not number.isdigit():
            return jsonify({"error": True, "message": "Invalid input. Please provide a valid number."}), 400
        
        number = int(number)
        properties = get_number_properties(number)
        
        # Fetching fun fact from Numbers API
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json")
        fun_fact = fun_fact_response.json().get("text", "No fact available")
        
        response = {
            "number": number,
            "is_prime": False,  # You can add logic to check for prime numbers
            "is_perfect": False, # You can add logic to check for perfect numbers
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

