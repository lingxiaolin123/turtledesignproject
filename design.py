
#my design
import turtle

turtle.colormode(255)#brings in the colormode function
turtle.bgcolor(200,150,100)

bob = turtle.Turtle()
bob.speed(11)
distance = 100

#using loop variable to change the value of color,distance.
for times in range(10):
    bob.begin_fill()
    bob.color(255,255,150-times)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.left(45)
    bob.forward(50)
    bob.goto(50,45)
    bob.end_fill()
    
for times in range(4):
    bob.color(150,255,100)
    bob.forward(100)
    bob.right(45)
    bob.forward(100)
    bob.right(45)


bob.forward(175)

for times in range(7):
    bob.color(100,230,255)
    bob.left(45)
    bob.forward(100)
    bob.left(45)
    bob.forward(100)

bob.right(45)

for times in range(4):
    bob.color(255,200,250)
    bob.forward(100)
    bob.right(45)
    bob.forward(100)
    bob.right(45)
    
bob.forward(200)

for times in range(4):
    bob.color(31,131,231)
    bob.left(45)
    bob.forward(100)
    bob.left(45)
    bob.forward(100)

bob.color(255,235,190)
bob.right(45)
bob.forward(100)
bob.left(90)
bob.forward(250)
bob.left(90)
bob.forward(500)
bob.left(90)
bob.forward(250)
bob.left(90)
bob.forward(100)

bob.color(205,240,100)
bob.right(90)
bob.forward(350)
bob.left(90)
bob.forward(300)
bob.left(90)
bob.forward(350)

bob.right(90)
bob.forward(50)
bob.color(255,0,255)
bob.right(90)
bob.forward(400)
bob.right(90)
bob.forward(300)
bob.forward(100)
bob.right(90)
bob.forward(400)

