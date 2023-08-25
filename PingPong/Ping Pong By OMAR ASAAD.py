# Name : Omar Asaad Sayed
# Code : 619183

# controls :
# Racket 1(The one on the left) is moved by pressing (W ,S) keys to move it up and down
# Racket 2 is moved by using the regular up and down controls


# importing turtle module
import turtle

wind = turtle.Screen()  # initialize screen
wind.title('MY FIRST GAME')  # set the title of the window
wind._bgcolor("black")  # set the background colour of the window
wind.setup(width=800, height=600)  # set the width and the height of the window
wind.tracer(0)  # stops the window from updating automatically

# racket 1
racket1 = turtle.Turtle()  # initializes turtle object(Shape)
racket1.speed(0)  # set the speed of the animation
racket1.shape("square")  # set the shape of the object(The shape of the racket)
racket1.color("red")  # set the color of the object (The color of the racket)
racket1.shapesize(stretch_len=1, stretch_wid=5)  # stretches the shape of  the size
racket1.penup()  # stop the objects from drawing lines
racket1.goto(-360, 0)  # set the position of the object at the beginning

# racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("yellow")
racket2.shapesize(stretch_len=1, stretch_wid=5)
racket2.penup()
racket2.goto(360, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0  |  Player 2: 0", align="center", font=("Courier", 20, "normal"))


# functions
def racket1_up():
    y = racket1.ycor()  # get the y coordinate of Racket 1
    y += 20  # set the y to increase by 20
    racket1.sety(y)  # set the y of Racket 1 to the new y coordinate


def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)


def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)


# keyboard binding
wind.listen()  # tell the keyboard to expect keyboard input
wind.onkeypress(racket1_up, "w")  # when pressing w the function racket1_p will be called
wind.onkeypress(racket1_down, "s")  # and so on
wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")
# main game loop
while True:
    wind.update()  # updates the window every time the loop runs
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at zero and every time loops run---> +2.5 on the x axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at zero and every time loops run---> +2.5 on the x axis

    # border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290:  # if the ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, making +2.5----> -2.5

    if ball.ycor() < -290:  # if ball at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse x direction (the direction of the ball)
        score1 += 1
        score.clear()
        score.write("Player1: {} | Player2: {}".format(score1, score2), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1: {} | Player2: {}".format(score1, score2), align="center", font=("Courier", 20, "normal"))

    # rackets collapes
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

#note : i couldn't upload an explaining video with it because i had no enough internet to
#download  a screen recorder program, i recorded a video with my mobile though bur it was
#too large to be uploaded on the site so i just kept it with explaining comments 
