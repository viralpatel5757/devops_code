import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

name_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}
name_dict = {row.letter:row.code for (index, row) in name_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter the name: ").upper()
phonetic_code_list = [name_dict[letter] for letter in word]
print(phonetic_code_list)

# long method to do above one line code is as below
# name_list = list(word)
# phonetic_code_list = []
# for letter in name_list:
#     if letter in name_dict:
#         phonetic_code_list.append(name_dict[letter])










