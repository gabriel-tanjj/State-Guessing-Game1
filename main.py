import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
# Getting entire column of data of "state" and converting it into a list format
all_states = data.state.tolist()
guessed_states = []

answer = screen.textinput(title=f"len{guessed_states}/50 States Guessed",
                          prompt="What is another state's name?").title()

while len(guessed_states) < 50:
    if answer == "Exit":
        break

    if answer in all_states:
        guessed_states.append(answer)
        turtle = turtle.Turtle()
        turtle.penup()
        turtle.hideturtle()
        # Checking which state matches the answer and
        # then returning the ROW of that state with all the columns inside it
        state_data = data[data.state == answer]
        # From there we can easily access the x and y coordinates by tapping into the variable state_data
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(answer)

missing_states = []

# To create a list of states not guessed

for states in all_states:
    if states not in guessed_states:
        missing_states.append(states)
    states_to_learn = pandas.DataFrame(missing_states)
    states_to_learn.to_csv("states_to_learn.csv")


screen.exitonclick()