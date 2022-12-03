# Define a function for each mathematical operation
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

# Prompt the user to enter two numbers and the operation they want to perform
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Use a conditional statement to call the appropriate function based on the operation entered by the user
if operation == "+":
  result = add(num1, num2)
elif operation == "-":
  result = subtract(num1, num2)
elif operation == "*":
  result = multiply(num1, num2)
elif operation == "/":
  result = divide(num1, num2)
else:
  print("Invalid operation")

# Print the result of the calculation
print(result)
