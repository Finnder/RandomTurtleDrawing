import turtle
import random

running = True

turtle.shape("turtle")
turtle.speed(30)
turtle.color("white")
turtle.bgcolor("black")

def randomNum():
    x = random.randint(1, 50)
    return x

def randomBack():
    x = random.randint(1, 10)
    return x

def randomColor():
    x = random.randint(0, 1)
    return x


while running:
    turtle.forward(randomNum())
    turtle.right(randomNum())
    turtle.color(randomColor(), randomColor(), randomColor())
    turtle.backward(randomBack())


