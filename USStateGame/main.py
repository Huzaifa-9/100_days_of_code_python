import turtle
import pandas
import time

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Games")
screen.setup(width=750, height=500)
image = "blank_states_img.gif"
# turtle.hideturtle()
screen.addshape(image)
turtle.shape(image)
guessed_states = []

game_is_on = len(guessed_states)
while game_is_on <= 50:
    answer_state = screen.textinput(title=f"{game_is_on}/50 States Correct",
                                    prompt="What's another state's name").title()
    # print(answer_state)
    if answer_state == "Exit":
        # states to learn

        states = data["state"]
        all_states = states.to_list()
        learn = [state for state in all_states if state not in guessed_states]
        data_dict = {
            "States": learn,
        }
        df = pandas.DataFrame(learn)
        df.to_csv("learn_states.csv")
        break

    states = data[data["state"] == answer_state]
    if len(states) != 0 and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        # print(states.x.item())
        # print(states.y.item())
        # print(guessed_states)
        x_col = states["x"].to_list()
        y_col = states["y"].to_list()
        text.goto(x_col[0], y_col[0])
        text.write(answer_state)
        game_is_on += 1

    else:
        text_2 = turtle.Turtle()
        text_2.penup()
        text_2.hideturtle()
        text_2.goto(-100, 0)
        text_2.write("Wrong. Guess again", align="center", font=("courier", 14, "normal"))
        time.sleep(1)
        text_2.clear()



screen.exitonclick()
