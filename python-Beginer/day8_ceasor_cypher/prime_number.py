# in this we will lear about, 
# functions with inputs
# positional VS keyword arguments

# function with inputs
def greet(name):  # here name is parameter
  print(f"hello {name}\n")
  print(f"hoe are you {name}\n")
  print(f"goodby {name}!!")

greet("viral")  # here viral is an argument

#############################################################################
# primt number

def prime_checker(number):
  if number > 1:
    flag = False
    for i in range(2,number):
      if number % i == 0:
        flag = True
        break
    if flag:
      print("number is not prime number")
    else:
      print("number is prime number")      

n = int(input("Check this number: "))
prime_checker(number=n)