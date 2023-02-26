# random module (it creates random outcome) 

import random
random_int = random.randint(1,100) # prints the random integer number b/w 1 and 100
print (random_int)
random_float = random.random() # prints random float b/w 0.00000.. and 0.9999999...  (multipling it with 5 so we get number b/w 0 and 5)
print (5 * random_float)

# heads or tails
import random
random = random.randint(1,2)
if random == 1:
 print ("Heads")
else:
  print("Tails")

###################################################################################################################
# Python List
fruits = ["apple", "banana", "cherry"]

fruits[0] = "orange" # it will replace "apple" with "orange" 
fruits.append("kiwi") # will add kiwi in to the list (in the last place afetr cherry)

# Python code to convert string to list character-wise
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

str1="ABCD"
print(Convert(str1))

# covert list in string
display = ["C", "A", "M", "E", "L"]
print(f"{' '.join(display)}")


# split the bill : Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # this will convert inputs in to list formates
X = len(names) - 1 
A = random.randint(0,X) # will generate a random number which will be use as index for abobe list and voila !!
print(names[A] + " is going to pay the bill today")

# nested list : it is a list inside another list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

# emoji replacement
row1 = ["🤩","💩","🤬"]
row2 = ["😵","🤢","🤪"]
row3 = ["🤑","🥵","😇"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

c = int(position[0]) - 1
r = int(position[1]) - 1
map[r][c] = "X"

print(f"{row1}\n{row2}\n{row3}")























