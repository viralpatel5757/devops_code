from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
go_on = True
bid_auction = {}



while go_on is True:
    name = input("What is your name ?: ")
    bid = input("what is your bid ?: $")
    bid_auction[name] = bid
    flow = input("do you still wanna go_on ? type 'yes' or 'no': ")
    if flow == "no":
        go_on = False
    else:
        clear()  

# max_bid = max(bid_auction.values())
# print(f"the max bid is {max_bid}") 
Heighest_bid = 0
for keys in bid_auction:
    bid_value = int(bid_auction[keys])
    if bid_value > Heighest_bid :
        Heighest_bid = bid_value
        winner = keys

print(f"the winner is {winner} and he bid ${Heighest_bid}")
