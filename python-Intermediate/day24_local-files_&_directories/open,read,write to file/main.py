# how to open, read write to file using "with" key word.

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

################  using "with" keyword  ####################

# with open("my_file.txt") as file:  # when you use with method you don't have to use .close()
#     contents = file.read()
#     print(contents)

########### writing to the file #############

# with open("my_file.txt", mode="w") as file:
#     file.write("added new text !!")

######### append to file ###########

# with open("my_file.txt", mode="a") as file:
#     file.write("\nadded new text !!")

########## opening file from different folder #######

with open(r"C:\Users\Viralkpatel\Desktop\example.txt") as file: # put "r" which converts normal string to raw string
    cont = file.read()
    print(cont)

