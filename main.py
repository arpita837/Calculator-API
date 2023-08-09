import requests

def main():
    operator = input("Enter operator (+, -, *, /): ")
    operand1 = float(input("Enter operand 1: "))
    operand2 = float(input("Enter operand 2: "))
    
    payload = {'operand1': operand1, 'operand2': operand2}
    response = requests.post(f'http://localhost:0.0.0.0/0/{operator}', json=payload)
    
    if response.status_code == 200:
        result = response.json().get('result')
        if result is not None:
            print(f"Result: {result}")
        else:
            print("Error:", response.json().get('error', 'An error occurred'))
    else:
        print("Error:", response.text)

if __name__ == '__main__':
    main()
