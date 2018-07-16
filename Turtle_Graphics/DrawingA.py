import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing an A')

#get default turtle and hide
the_turtle = turtle.getturtle()
#the_turtle.hideturtle()

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
the_turtle.setposition(-100, 0)
the_turtle.pendown()
the_turtle.setposition(0,250)
the_turtle.setposition(100,0)
the_turtle.penup()
the_turtle.setposition(-64,90)
the_turtle.pendown()
the_turtle.setposition(64,90)


the_turtle.speed(10)


turtle.exitonclick()
