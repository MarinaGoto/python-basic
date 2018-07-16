# P 1. p. 244 
#Give a set of instructions for controlling the turtle to draw a line from the top-left corner of the screen 
#to the bottom-right corner, and from the top-right corner to the bottom-left corner, 
#thereby making a big X on the screen. There should be no other lines drawn on the screen. 

import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing an X')

#get default turtle and hide
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

#shape
the_turtle.shape('turtle')
the_turtle.fillcolor('black')

#color
turtle.colormode(255)
the_turtle.pencolor(169, 71, 169)

#size
the_turtle.pensize(41)
#resize
the_turtle.resizemode('user')
the_turtle.turtlesize(3, 3)

#create square (absolute postioning)
the_turtle.penup()
the_turtle.setposition(-400, 300)
the_turtle.pendown()
the_turtle.setposition(400, -300)
the_turtle.penup()
the_turtle.setposition(400,300)
the_turtle.pendown()
the_turtle.setposition(-400,-300)



the_turtle.speed(1)


turtle.exitonclick()