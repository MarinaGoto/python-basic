# P.3 p. 244
# Give a set of instructions for controlling the turtle to draw the letter W using relative positioning. 


import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing a letter W')

#get default turtle and hide
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

#shape
the_turtle.shape('turtle')
the_turtle.fillcolor('black')

#color
turtle.colormode(255)
the_turtle.pencolor(169, 71, 19)

#size
the_turtle.pensize(4)
#resize
the_turtle.resizemode('user')
the_turtle.turtlesize(3, 3)

#create square (relative postioning)
the_turtle.right(65)
the_turtle.forward(100)
the_turtle.left(135)
the_turtle.forward(50)
the_turtle.right(135)
the_turtle.forward(50)
the_turtle.left(135)
the_turtle.forward(100)



the_turtle.speed(1)


turtle.exitonclick()