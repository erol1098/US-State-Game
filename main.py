import turtle
import pandas

name = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S States Game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("./50_states.csv")

liste = data.state.to_list()

correct_answers =[]

is_end = False
while not is_end:
    
    answer = (screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Enter a state's name:")).title()
    state = data[data.state == answer]
    if answer == "Exit":
        missing_states = [state for state in liste if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("For Learning.csv")
        break
    if answer in liste:
        correct_answers.append(answer)
        name.hideturtle()
        name.penup()
        name.goto(int(state.x),int(state.y))
        name.write(state.state.item())
        if len(correct_answers) == 50:
            is_end = True
            name.goto(-220, 220)
            name.write("Congrats! You guessed all states.", font= ("Courier", 15, "bold"))
    
screen.exitonclick()


# # ekrnda tıklanan yerin koordinatını alır
# import turtle

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()