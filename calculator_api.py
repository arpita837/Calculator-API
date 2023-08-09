from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    operand1 = data['operand1']
    operand2 = data['operand2']
    result = operand1 + operand2
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    operand1 = data['operand1']
    operand2 = data['operand2']
    result = operand1 - operand2
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    operand1 = data['operand1']
    operand2 = data['operand2']
    result = operand1 * operand2
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    operand1 = data['operand1']
    operand2 = data['operand2']
    if operand2 == 0:
        return jsonify({'error': 'Division by zero is not allowed'})
    result = operand1 / operand2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
