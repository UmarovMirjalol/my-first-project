number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
       
    
    else:
        return "Invalid operation"

result = calculate(number1, number2, operation)
print("Result:", result)