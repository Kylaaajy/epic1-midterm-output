import turtle
turtle.speed(0)
turtle.bgcolor("black")

for i in range(15):
    for colours in ["brown", "yellow", "orange"]:
        turtle.setpos(0,0)
        turtle.color(colours)
        turtle.pensize(2)
        turtle.left(12)
        turtle.forward(220)
        turtle.left(90)
        turtle.forward(220)
        turtle.left(90)
        turtle.forward(220)
        turtle.left(90)

for i in range(36):
    turtle.setpos(0,2)
    turtle.color("purple")
    turtle.speed(11)
    turtle.circle(100)
    turtle.color("violet")
    turtle.forward(200)
    turtle.left(120)
    turtle.color("magenta")
    turtle.forward(100)
    turtle.right(120)
    turtle.left(170)
    turtle.left(20)
    turtle.forward(15)
turtle.done