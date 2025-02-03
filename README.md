# Flask API: Number Classification and Fun Facts

This is a Flask-based API that accepts a number and returns interesting mathematical properties (e.g., whether it's prime, perfect, Armstrong, odd, or even) along with a fun fact about the number.

## Table of Contents

1. [Project Description](#project-description)
2. [Requirements](#requirements)
3. [Installation Instructions](#installation-instructions)
4. [Running the API](#running-the-api)
5. [API Usage](#api-usage)
6. [License](#license)

## Project Description

This project is a simple API built using **Flask**, which classifies a number and returns JSON formatted information, including:
- Whether the number is prime.
- Whether the number is a perfect number.
- Other properties like Armstrong, odd, or even.
- A fun fact about the number (using an external service for fun facts).

## Requirements

- **Python 3.x** or higher
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)

The required packages are listed in the `requirements.txt` file.

## Installation Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:
bash
Copy
Edit
cd your-repository-name
Install the required dependencies:
bash
Copy
Edit
pip install -r requirements.txt

Running the API
After installing the dependencies, you can run the API locally with:
bash
Copy
Edit
python app.py
The API will run on http://127.0.0.1:5000.
API Usage
Endpoint:
GET /api/classify-number?number=<number>

Example request:

typescript
Copy
Edit
GET /api/classify-number?number=371
Example response:
json
Copy
Edit
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Error Response (if the input is not valid):
json
Copy
Edit
{
  "number": "alphabet",
  "error": true
}
License
This project is licensed under the MIT License - see the LICENSE file for details.

csharp
Copy
Edit
