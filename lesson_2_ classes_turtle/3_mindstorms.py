import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")

    brad= turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed (2)

    line=1
    while line < 5:
        brad.forward(100)
        brad.right(90)
        line=line+1

def draw_circle():
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    mari=turtle.Turtle()
    mari.shape()
    mari.color("green")
    mari.speed(5)

    li=1
    while li < 4:
        mari.fd(100)
        mari.left(120)
        li=li+1
    


    window.exitonclick()

draw_square()
draw_circle()
draw_triangle()
