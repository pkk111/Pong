import turtle
import os
from time import perf_counter

#           Player controls
#       Player A        Player B
# Up :    W/w            up-key
# Down :  S/s            down-key
# Evil laugh :  l/L
# Laugh :       ;
# Anger :       '

#Game variables
ball_speed = 0.2
plank_dist_moved = 20
levelup_time = 2
bgcolor = "black"
ball_color = "white"
plank_color = "green"
score_color = "orange"

#Score 
score_a = 0;
score_b = 0;

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor(bgcolor)
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.color(plank_color)
pad_a.penup()
pad_a.goto(-350, 0)

#Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color(plank_color)
pad_b.penup()
pad_b.goto(350,0)

#Ball defining
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(ball_color)
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

#Pen for score displaying
pen = turtle.Turtle()
pen.speed(0)
pen.color(score_color)
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0    Player B:0", align="center", font=("Courier",24, "normal"))

#Movement functions
def paddle_a_up():
    y = pad_a.ycor()
    if y < 250:
        y += plank_dist_moved
    pad_a.sety(y)

def paddle_a_down():
    y = pad_a.ycor()
    if y > -250:
        y -= plank_dist_moved
    pad_a.sety(y)

def paddle_b_up():
    y = pad_b.ycor()
    if y < 250:
        y += plank_dist_moved
    pad_b.sety(y)

def paddle_b_down():
    y = pad_b.ycor()
    if y > -250:
        y -= plank_dist_moved
    pad_b.sety(y)

def evil_laugh():
    os.system("aplay Evil_Laugh_Male.wav&")

def laugh():
    os.system("aplay Chuckle.wav&")

def anger():
    os.system("aplay Angry_Pirate.wav&")


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(evil_laugh, "l")
wn.onkeypress(evil_laugh, "L")
wn.onkeypress(laugh, "semicolon")
wn.onkeypress(anger, "apostrophe")

os.system("aplay Robot_blip.wav&")   #& makes sound playing asyncronous
start_time = perf_counter()
t=0;

#Main game loop
while True:
    wn.update()
    
    elapsed_time = perf_counter() - start_time
    if elapsed_time - t > levelup_time:
        t = elapsed_time
        ball.dx += ball.dx/10;
        ball.dy += ball.dy/10;
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1;
        os.system("aplay bounce_soft.wav&")   #& makes sound playing asyncronous
    
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1;
        os.system("aplay bounce_soft.wav&")   #& makes sound playing asyncronous
    
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.dx *= -1;
        pen.clear()
        if ball.xcor() >= 390:
            score_a += 1
            pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))
        else:
            score_b += 1
            pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "normal"))
        ball.goto(0,0)
        ball.dx = ball_speed
        ball.dy = ball_speed
        os.system("aplay Robot_blip.wav&")   #& makes sound playing asyncronous
    
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < pad_b.ycor()+50 and ball.ycor() > pad_b.ycor()-50):
        ball.setx(330)
        ball.dx *= -1
        os.system("aplay bounce_hard.wav&")   #& makes sound playing asyncronous
    
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < pad_a.ycor()+50 and ball.ycor() > pad_a.ycor()-50):
        ball.setx(-330)
        ball.dx *= -1
        os.system("aplay bounce_hard.wav&")   #& makes sound playing asyncronous