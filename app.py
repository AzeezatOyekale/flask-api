from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
        num = request.args.get("number")
        if not num.isdigit():
            return jsonify({"number": num, "error": True}), 400

        num = int(num)
        properties = get_number_properties(num)
        digit_sum = sum(int(d) for d in str(num))

        # Get a fun fact from the Numbers API
        fun_fact = requests.get(f"http://numbersapi.com/{num}/math").text

        return jsonify({
            "number": num,
            "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
            "is_perfect": num == sum(i for i in range(1, num) if num % i == 0),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
