# List Comprehension
# syntax is as below
# new_list = [new_item for item in existing_list]

import random

numbers = [1, 2, 3]
new_number_list = [n+1 for n in numbers]
print(new_number_list)

# works with string as well
name = "Viral"
new_name_list = [letter for letter in name]
print(new_name_list)

# works with range module.
new_range_list = [n*2 for n in range(1, 5)]
print(new_range_list)

# you can imbibe if condition in it as well
# syntax: new_list = [new_item for item in existing_list if test]

names = ["Viral", "Mikin", "Amrut", "Panth", "alex", "ami"]
five_letter_name = [name for name in names if len(name) == 5 ]
print(five_letter_name)

############################# Dictionary Comprehension ################################################################

# syntax: new_dict= {new_key:new_value for item in list}
# syntax: new_dict= {new_key:new_value for (key,value) in dict.item() }
# syntax: new_dict= {new_key:new_value for (key,value) in dict.item() if test }

# assing random score to students.
students_names = ["Viral", "Mikin", "Amrut", "Panth", "alex", "ami"]
student_score = {name:random.randint(1, 100) for name in students_names}
print(student_score)

# make dict of all students with >= 60 score
passed_students = {name:score for (name, score) in student_score.items() if score >= 60}
print(passed_students)

# convert C to F temperature value
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
print(weather_f)

############################### Pandas iterrows() method ########################

import pandas

student_dict = {
    "students": ["viral", "mikin", "panth"],
    "score": [90, 85, 88]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    print(row)

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}
















