# go to line 38 to see the usage of list comprehension

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) # this turtle shows the image in background
state_name_turtle = turtle.Turtle() # this turtle will go to (x,y) and then write the name of the state on screen
state_name_turtle.hideturtle()

score = 0

states_coordinates = pandas.read_csv("50_states.csv") # get the dataframe
states_coordinates_list = states_coordinates["state"].to_list() # convert the dataframe in to list
guessed_state_list = []

while score < 51:
    answer = screen.textinput(title=f"Guess the state, score: {score}/50",
                              prompt="write the name of next state here !!").title()
    if answer == "Exit":
        break
    elif answer in states_coordinates_list:
        state_row = states_coordinates[states_coordinates["state"] == answer]  # from dataframe find specific row
        X = int(state_row["x"])
        Y = int(state_row["y"])
        state_name_turtle.penup()
        state_name_turtle.goto(X, Y)
        state_name_turtle.write(answer, align="center", font=("Courier", 8, "normal"))
        score += 1
        guessed_state_list.append(answer)
    else:
        pass

# print out the remaining states to saparate CSV file.
remaining_states = [state for state in states_coordinates_list if state not in guessed_state_list ]
remaining_states_df = pandas.DataFrame(remaining_states)
remaining_states_df.to_csv("remaining_states.csv")


