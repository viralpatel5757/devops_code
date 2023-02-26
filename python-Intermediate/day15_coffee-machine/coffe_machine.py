MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}

coffee_selection = ""
Total = 0
refund = 0
go_on = True
enough_resources = True


def resource_update():
    global enough_resources
    if coffee_selection == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        else:
            enough_resources = False
            return print("Not enough Water")
        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        else:
            enough_resources = False
            return print("Not enough coffee")

    elif coffee_selection == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        else:
            enough_resources = False
            return print("Not enough water")
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        else:
            enough_resources = False
            return print("Not enough milk")
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        else:
            enough_resources = False
            return print("Not enough coffee")

    elif coffee_selection == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        else:
            enough_resources = False
            return print("Not enough water")
        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        else:
            enough_resources = False
            return print("Not enough milk")
        if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        else:
            enough_resources = False
            return print("Not enough coffee")


def coin_update():
    global refund
    if coffee_selection == "espresso":
        if Total >= MENU["espresso"]["cost"]:
            refund = Total - MENU["espresso"]["cost"]
            resources["Money"] += MENU["espresso"]["cost"]
            return print(f"Here is your change ${refund}")
        else:
            print("Not enough Money !!")
    elif coffee_selection == "latte":
        if Total >= MENU["latte"]["cost"]:
            refund = Total - MENU["latte"]["cost"]
            resources["Money"] += MENU["latte"]["cost"]
            return print(f"Here is your change ${refund}")
        else:
            print("Not enough Money !!")
    elif coffee_selection == "cappuccino":
        if Total >= MENU["cappuccino"]["cost"]:
            refund = Total - MENU["cappuccino"]["cost"]
            resources["Money"] += MENU["cappuccino"]["cost"]
            return print(f"Here is your change ${refund}")
        else:
            print("Not enough Money !!")


while go_on:
    coffee_selection = input("what would you like? (espresso/latte/cappuccino): ")
    if coffee_selection == "report":
        print(resources)
    else:
        resource_update()
        if enough_resources:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            penny = int(input("How many penny?: "))
            Total = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (penny*0.01)
            coin_update()
        else:
            continue

print(resources)

