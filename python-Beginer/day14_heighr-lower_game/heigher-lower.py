from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

current_score = 0

item_A = random.choice(data)

def check():
    print(f'Compare A = {item_A["name"]}, {item_A["description"]}, from {item_A["country"]}')
    print(vs)
    print(f'Against B = {item_B["name"]}, {item_B["description"]}, from {item_B["country"]}')

    followers_A = int(item_A["follower_count"])
    followers_B = int(item_B["follower_count"])

    if followers_A > followers_B:
        response = "A"
        return response
    else:
        response = "B"
        return response

go_on = True         
while go_on :
    item_B = random.choice(data)
    while item_A == item_B:
        item_B = random.choice(data)
    answer = check()
    user_choice = input("who has more followers ? Type 'A' or 'B': ").upper()
 
    if user_choice == answer :
        current_score += 1
        item_A = item_B
        clear()
        print(f"you are right ! current score is {current_score}")
    else:
        print(f"sorry that's wrong !! you lose with score {current_score}") 
        go_on = False 