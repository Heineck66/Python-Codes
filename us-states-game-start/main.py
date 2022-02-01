import turtle
import pandas

screen = turtle.Screen()
screen.title("States names")

image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

states = {}
data = pandas.read_csv("50_states.csv")

for state in data["state"]:
    state_data = data[data["state"] == state]
    states[state] = (int(state_data.x), int(state_data.y))

total = 0
while total < 50:
    anwser = turtle.textinput(
        title=f"{50 - len(states)}/50 states", prompt="Give an state name:"
    ).title()

    print(anwser)

    if anwser == "Exit":
        break

    if anwser in states:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(states[anwser])
        state.write(f"{anwser}")
        states.pop(anwser)
        total += 1
        print(total)

with open("states_to_learn.csv", "w") as file:
    for state in states:
        file.write(f"{state}\n")

screen.exitonclick()
