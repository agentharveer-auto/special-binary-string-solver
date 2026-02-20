from flask import Flask, request, jsonify
from special_binary_string import special_binary_string  # Import the algorithm

app = Flask(__name__)

@app.route('/api/solve', methods=['POST'])
def solve_endpoint():
    data = request.get_json()
    input_string = data.get('string')

    # Input Validation (Backend)
    if not isinstance(input_string, str) or not all(c in '01' for c in input_string):
        return jsonify({'error': 'Invalid input string'}), 400

    result = special_binary_string(input_string)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)