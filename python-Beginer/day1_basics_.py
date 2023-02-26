print("hello world !!")

# input() : asks user to enter his name
# len() : counts the lettrs of the name
# print() : prints how many letters are there in user's name.
print(len(input("enter your name:")))

# storing the bvalue inside variable and then print it.
name = input("What is your name?")
print("hello" + name)

#############################################################################################################

#1. Create a greeting for your program.
print("welcoem to band-name-generator")
#2. Ask the user for the city that they grew up in.
city = input("what is name of city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("what is name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band could be" + " " + city + " " + pet)

#escaping charater
turn1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"') # here \ is escaping char as ' counts as string and not end of first '