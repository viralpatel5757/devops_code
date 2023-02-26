#Functions with Outputs 

def format_name(f_name, l_name):
  """ Take first and last name and convert it to Title Case""" # this is doc string (when you hover over the function name it shows this info) 
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." # (multiple return statemnents)
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

formatted_name = format_name(input("Your first name: "), input("Your last name: "))  # Storing output in a variable
print(formatted_name)  # printing that variable

####################################################################################
# leap year with functions

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True # print("Leap year.")
      else:
        return False # print("Not leap year.")
    else:
      return True # print("Leap year.")
  else:
    return False # print("Not leap year.")

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
      return leap_year_month_days[month-1]
  else:
      return  month_days[month-1]   
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days) 