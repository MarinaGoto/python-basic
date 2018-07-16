#P 2. p. 244
#Using relative positioning, give a set of instructions for controlling the turtle to draw an isosceles triangle
#on the screen (that is, a triangle with two equal-length sides). 


import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing an isosceles triangle')

#get default turtle and hide
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

#shape
the_turtle.shape('turtle')
the_turtle.fillcolor('black')

#color
turtle.colormode(255)
the_turtle.pencolor(169, 171, 169)

#size
the_turtle.pensize(41)
#resize
the_turtle.resizemode('user')
the_turtle.turtlesize(3, 3)

#create square (absolute postioning)
the_turtle.penup()
the_turtle.setposition(-300, -200)
the_turtle.pendown()
the_turtle.setposition(0, 0)
the_turtle.pendown()
the_turtle.setposition(300,-200)
the_turtle.pendown()
the_turtle.setposition(-300,-200)



the_turtle.speed(1)


turtle.exitonclick()