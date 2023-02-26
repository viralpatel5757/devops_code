# python dictionaries + Nesting
# dictionery has key and value  (if the key and value information is so long use the indentation as below)
# list only has simple values (no keys.)
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# retriving item from dictionary (you will need to provide key)
print(programming_dictionary["Bug"])

# adding key:value to existing dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# creating an empy dictionary 
empy_dict = {}

# editing an existing dict.
programming_dictionary["Bug"] = "it is edited Bug" # so it will update the valu of key 'Bug' in programming_dictionary

# loop through dictionary
for key in programming_dictionary:
    print(key)  # it will print all the keys
    print(programming_dictionary[key]) # it will print all the values

###############################################################################################################
# example of dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91 :
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90 :
        student_grades[key] = "Exceeds Expectations" 
    elif 71 <= student_scores[key] <= 80 :
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70 :
        student_grades[key] = "Fail" 

print(student_grades)

##################################################################################
# Nesting Dictionaries and Lists
# dict1 = {key1: [list1], key2 : {dict2}}

capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
###################################################################################################
# print specific iteam
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak", "chicken"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0]) # this will print "steak"

######################################################################################################
# coding chalange : add an item to list which consist dictionary 
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country (country, visits, cities) :
    log = {} 
    log["country"] = country
    log["visits"] = visits
    log["cities"] = cities
    travel_log.append(log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log) 


