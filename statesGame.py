import turtle
import pandas
import os
import pathlib

screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
learn_states_file = pathlib.Path("states_to_learn.csv")

correct_states=[]

while len(correct_states) < 50:
    if learn_states_file.exists():
        os.remove("states_to_learn.csv")
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_states:
                missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        correct_states.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == answer_state]
        state.goto(state_data.x.item(),state_data.y.item())
        state.write(answer_state)


