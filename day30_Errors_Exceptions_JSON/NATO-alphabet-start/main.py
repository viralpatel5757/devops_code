# if user enters something other thatn aplphabet a exception should trigger saying "only letters please"

import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

name_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
name_dict = {row.letter:row.code for (index, row) in name_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter the name: ").upper()
    try:
        phonetic_code_list = [name_dict[letter] for letter in word]
    except KeyError:
        print("only letters please")
        generate_phonetic()
    else:
        print(phonetic_code_list)

generate_phonetic()












