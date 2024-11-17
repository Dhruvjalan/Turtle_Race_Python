from turtle import Turtle, Screen
import random

#tim = Turtle()
# def move_forward():
#     tim.forward(10)
#
# def move_back():
#     tim.back(10)
#
# def ccw():
#     tim.left(10)
#
# def cw():
#     tim.right(10)
#
# def clear():
#     screen.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=ccw)
# screen.onkey(key="d", fun=cw)
# screen.onkey(key="c", fun=clear)
screen = Screen()
play=True
winner=""

t_green=Turtle()
t_green.color("Green")
t_purple=Turtle()
t_purple.color("Purple")
t_red=Turtle()
t_red.color("Red")
t_yellow=Turtle()
t_yellow.color("Yellow")

turtles = [t_green, t_purple, t_red, t_yellow]
for i in range(4):
    turtles[i].up()
    turtles[i].sety(50*i)
    turtles[i].setx(-350)

bet = screen.textinput("Place your bet","Who do you think will win? Green/Purple/Red/Yellow")
#print(t_yellow.xcor())
while play:
    for i in range(4):
        turtles[i].forward(random.randrange(0,50))
        # print(turtles[i].xcor())
        if turtles[i].xcor()>=350:
            winner=turtles[i]
            play=False


if play==False:
    if winner.color()[0]==bet:
        print(f"You win, the winner was {winner.color()[0]}")
    else:
        print(f"You lose, the winner was {winner.color()[0]}, you bet on {bet}")
screen.exitonclick()