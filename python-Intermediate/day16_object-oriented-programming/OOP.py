from turtle import Turtle, Screen
jerry = Turtle()
my_screen = Screen()

jerry.shape("turtle")
jerry.color("green")
jerry.forward(100)
print(jerry)
my_screen.exitonclick()

###############################################

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Charmender", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"

print(table)
