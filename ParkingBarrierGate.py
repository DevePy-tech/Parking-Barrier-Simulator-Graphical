# Importing turtle module
import turtle
from time import sleep

# Creating Turtle
t = turtle.Turtle()

def set_position(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Rectangle Function
def draw_gate():
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.right(90)

def draw_gate_arm(angle, color):
    t.color(color)
    t.pensize(5)
    t.left(angle)
    t.forward(180)

def draw_drive_motor():
    t.color("blue","blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def open_gate_arm():
    angle = 90
    velocity = 5
    r = int(angle / velocity)
    for i in range(r):
        #print(i)
        set_position(-240, 25)
        draw_gate_arm(0, "white")
        t.speed(0)
        set_position(-240, 25)
        draw_gate_arm(velocity, "blue")
        t.speed(0.5)
        
def close_gate_arm():
    angle = 90
    velocity = 5
    r = int(angle / velocity)
    for i in range(r):
        #print(i)
        set_position(-240, 25)
        draw_gate_arm(0, "white")
        t.speed(0)
        set_position(-240, 25)
        draw_gate_arm(-velocity, "blue")
        t.speed(0.5)

def control_gate_arm(direction):  
    angle = 90
    velocity = 0
    if direction == "up":
        velocity = 5    
    elif direction == "down":
        velocity = -5
    else:
        return

    r = int(angle / abs(velocity))
    #print(r)

    for i in range(r):
        #print(i)
        set_position(-240, 25)
        draw_gate_arm(0, "white")
        t.speed(0)
        set_position(-240, 25)
        draw_gate_arm(velocity, "blue")
        t.speed(0.5)


def init():
    t.speed(0)
    #t.hideturtle()
    set_position(-300, 100)
    t.color("black","gray")
    t.begin_fill()
    draw_gate()
    t.end_fill()

    set_position(-50, 100)
    t.color("black","gray")
    t.begin_fill()
    draw_gate()
    t.end_fill()

    set_position(-250, 12.5)
    draw_drive_motor()
    set_position(-240, 25)
    draw_gate_arm(0, "blue")


def show_demo1():
    init()
    open_gate_arm()
    close_gate_arm()
    input("Press a key to close... ")
    print("bye")

def show_demo2():
    init()
    control_gate_arm("up")
    control_gate_arm("down")
    input("Press a key to close... ")
    print("bye")


# Hiding the turtle
t.hideturtle()


# Calling demo
#show_demo1()
#show_demo2()

