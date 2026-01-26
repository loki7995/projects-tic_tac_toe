# Basic Calculator Program
print("Basic Calculator")
print("Supported operators: +, -, *, /, %")

# Get input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ").strip()
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/' and num2 != 0:
    result = num1 / num2
elif operator == '%' and num2 != 0:
    result = num1 % num2
else:
    result = "Error: Invalid operator or division/modulo by zero"

# Display result
print(f"Result: {result}")


#OUTPUT
'''Basic Calculator
Supported operators: +, -, *, /, %
Enter first number: 98
Enter operator (+, -, *, /, %): +
Enter second number: 2
Result: 100.0'''
