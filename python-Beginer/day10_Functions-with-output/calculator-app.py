# add
def add(n1,n2):
    return n1 + n2

# subtract
def sub(n1,n2):
    return n1 - n2

# multiplication
def mul(n1,n2):
    return n1 * n2

# division
def div(n1,n2):
    return n1 / n2

operation = {
    "+":add, 
    "-":sub, 
    "*":mul, 
    "/":div 
}

num1 = int(input("first number: "))
num2 = int(input("second number: "))

for keys in operation:
    print(keys)
    
maths_sign = str(input("enter the operator: ")) 
calculation_function =  operation[maths_sign]
answer = calculation_function(num1,num2)

print(f"{num1} {maths_sign} {num2} = {answer}")
        
#####################################################################################################
# fine tune calculator

from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()