import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725,height=491)

turtle.shape(image)
tim = turtle.Turtle()
tim.up()
tim.hideturtle()
is_game_on = True
correct_response = list()

while is_game_on:
    if len(correct_response) == 50:
        is_game_on = False
    _state = screen.textinput(title=f"Correct {len(correct_response)}/50",prompt="Name a state")

    if not data[data.state == _state.capitalize()].empty and _state not in correct_response:
        correct_response.append(_state)
        x_axis = int(data[data.state == _state.capitalize()].x.iloc[0])
        y_axis = int(data[data.state == _state.capitalize()].y.iloc[0])
        tim.goto(x_axis,y_axis)
        tim.write(_state.capitalize())

screen.exitonclick()