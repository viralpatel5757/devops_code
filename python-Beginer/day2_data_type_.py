# data types : string , float, integer, boolean

# type() : is function to know the type of data
# here type() will return integer as len() is stored in name_lenght ans it is integer
name_lenght = len(input("enter name:\n"))
print(type(name_lenght))


# transfering integr data type in to string so that concatination works !!
name_len = len(input("enter name:\n"))
new_name_len = str(name_len)
print("your name has " + new_name_len + " characters")

# if you enter two digit number = 12 , then output will be 1+2 = 3
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
a = two_digit_number[0]
b = two_digit_number[1]
c = int(a) + int(b)
print(c)

# mathematic operators
3 + 5 # summation
3 - 5 # subtraction
3 * 5 # multiplication
3 / 3 # division
3 ** 3  # power so the answer here is 27
print(round(8 / 3))  # it gives 3 ,as 2.666666 gets converted to nearest round number
print(8 // 3) # gives 2, it gives unteger value and discards the floats.

# calculating the BMI (body mass index)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
w = float(weight)
h = float(height) ** 2
bmi = ( w/h)
print(int(bmi))

# f-string
score = 10
print(f"your score is {score}") # with f-string you can concate without manually converting everything to string data type.

#If the bill was $150.00, split between 5 people, with 12% tip. 

#tip calculator : Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("welcome to the tip calculator !!\n")
bill = float(input("what was the total bill ?\n"))
percentage = float(input("what % tip would you like to give :\n"))
final_percentage = 1 + (percentage / 100)
people = int(input("how many people to split the bill ?\n"))
tip = (bill / people) * final_percentage
final_tip = round(tip,2)
print(f"Each person shold pay: {final_tip}")





