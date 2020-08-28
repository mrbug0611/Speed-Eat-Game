from turtle import *
import random as rd

# randomizing the food locations
randomx = rd.randint(-390, 390)
randomy = rd.randint(-290, 290)

# sets value for score and movement speed of head
speed_up = 0.08
score = 0
high = 0

# create screen
wn = Screen()
wn.bgcolor('blue')
wn.title('Speed Eat')
wn.tracer(0)
wn.setup(800, 600)

# create turtle
head = Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 0)
head.dx = 0
head.dy = 0.08

# create food
food = Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.shapesize(stretch_wid=1, stretch_len=1)
food.penup()
food.goto(randomx, randomy)

# create score board
score_board = Turtle()
score_board.color('white')
score_board.penup()
score_board.goto(-370, 270)
score_board.pendown()
score_board.hideturtle()
score_board.write(f'Score: {score}                          High Score: {high}', font=('Courier', 16, 'normal'))


# change direction with arrow keys
def move_up():
    head.dx = 0
    head.dy = speed_up


def move_down():
    head.dx = 0
    head.dy = -speed_up


def move_left():
    head.dy = 0
    head.dx = -speed_up


def move_right():
    head.dy = 0
    head.dx = speed_up


# activates the key commands
wn.listen()
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')

# main loop of program
while True:
    wn.update()

    # updates stats when player eats food
    if food.xcor() + 10 >= head.xcor() >= food.xcor() - 10 and food.ycor() + 10 >= head.ycor() >= food.ycor() - 10:
        randomx = rd.randint(-390, 390)
        randomy = rd.randint(-290, 290)
        food.goto(randomx, randomy)
        speed_up += 0.02
        score += 10
        score_board.clear()
        score_board.write(f'Score: {score}                          High Score: {high}', font=('Courier', 16, 'normal'))

        # change score
        if score > high:
            high += 10
            score_board.clear()
            score_board.write(f'Score: {score}                          High Score: {high}',
                              font=('Courier', 16, 'normal'))

    # resets game when player hits border
    if head.xcor() >= 400 or head.xcor() <= -400 or head.ycor() >= 300 or head.ycor() <= -300:
        head.goto(0, 0)
        speed_up = 0.08
        score = 0
        score_board.clear()
        score_board.write(f'Score: {score}                          High Score: {high}',
                          font=('Courier', 16, 'normal'))

    # allows head to move
    head.setx(head.xcor() + head.dx)
    head.sety(head.ycor() + head.dy)
