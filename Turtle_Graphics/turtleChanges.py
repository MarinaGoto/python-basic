#Give a set of instructions that sets the turtle to an actual turtle shape, and moves it from the bottom of the
#screen towards the top, getting smaller as it moves along. 

import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing an turtle')

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

    
#create turtle
the_turtle.penup()
the_turtle.setposition(-400, -300)
the_turtle.pendown()
the_turtle.setposition(100,50)

#########################
  
#resize
the_turtle.resizemode('user')
the_turtle.turtlesize(10, 10)

    
#create turtle
the_turtle.penup()
the_turtle.setposition(100, 50)
the_turtle.pendown()
the_turtle.setposition(300,200)





the_turtle.speed(9)


turtle.exitonclick()





############################################

#incrice in loop 

import turtle
turtle.setup(800, 600)
window = turtle.Screen()
window.title('turtle sizes')
the_turtle = turtle.getturtle()
the_turtle.resizemode('user')
the_turtle.shape('turtle')
the_turtle.speed(9)

x_position = 0
y_position = 0
turtle_size = 10
while y_position < 200:
    the_turtle.setposition(x_position, y_position)
    the_turtle.turtlesize(turtle_size, turtle_size)
    the_turtle.stamp()
    x_position = x_position + 75
    y_position = y_position + 75
    turtle_size = turtle_size - 2
    
turtle.exitonclick()

