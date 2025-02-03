from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Test route for checking if the app is working
@app.route('/')
def hello():
    return "Flask API is running!"

# Test route for more debugging
@app.route('/test')
def test_route():
    return "Test route is working!"

def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    """Check if a number is perfect."""
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

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
        
        # Creating the response with additional prime and perfect number checks
        response = {
            "number": number,
            "is_prime": is_prime(number),  # Call is_prime function
            "is_perfect": is_perfect(number),  # Call is_perfect function
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
