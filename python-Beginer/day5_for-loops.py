# for loop

fruits = ["apple", "peach", "pear"]
for slice in fruits: # you can select any name instead of slice (it is variable)
  print(slice)

# excercise : count the avg height using for loop
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)
h = 0
i = 0

for height in student_heights:
 h += height
 i += 1 
print(round(h/i)) 

# excercise : print out hte heigst score out of the list
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

a = student_scores[0]
for n in student_scores:
  if n > a:
    a = n
  else:
    a = a
print(a)

# exersize: FizzBuzz game 
# print fizz for number divisible by 3
# print buzz for number divisible by 5
# print fizzbuzz for number divisible by 3 & 5 (like 15)
for i in range (0,101):
  if i % 3 == 0 and i % 5 == 0:
    print ("fizzbuzz")
  elif i % 3 == 0 :# and i % 5 == 0:
    print ("fizz")
  elif i % 5 == 0 :# and i % 5 == 0:
    print ("buzz")
  else :
    print (i) 

# exc : generate password with letters, symbols and numbers.
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for i in range(0,nr_letters):
    password_list += random.choice(letters)

for i in range(0,nr_symbols):
    password_list += random.choice(symbols)

for i in range(0,nr_numbers):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list :
   password += char

print(password)    







