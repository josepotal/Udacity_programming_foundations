# using turtle to discover Classes and objects

#"turtle" is a module
#"Turtle" is a class
# "brad" is an instance/object of the class that reponse to the functions


import turtle

def draw_square (some_turtle):
    for i in range(1,5):
        some_turtle.fd(100)
        some_turtle.right(90)


def draw_art ():
    window=turtle.Screen()
    window.bgcolor("red")
    #create turtle brad
    brad= turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed (5)

    for i in range (1,36):
        draw_square(brad)
        brad.right(10)
    
    #create turtle angie
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)


draw_art()
