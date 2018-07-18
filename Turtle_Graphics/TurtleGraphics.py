import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Absolute Positioning')

#get default turtle and hide
the_turtle = turtle.getturtle()
the_turtle.hideturtle()



#create square (absolute postioning)
the_turtle.forward(100)
the_turtle.left(90)
the_turtle.forward(100)
the_turtle.left(90)
the_turtle.forward(100)
the_turtle.left(90)
the_turtle.forward(100)
the_turtle.left(90)

the_turtle.speed(2)


turtle.exitonclick()
