#  Give a set of instructions that moves the turtle with an actual turtle shape from the bottom of the screen
# toward the top, changing its fill color when it crosses the x axis of the grid coordinates. 

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
    if x_position < 75:
        the_turtle.fillcolor('blue')
    elif x_position == 75 or x_position < 150:
        the_turtle.fillcolor('red')
    else:
        the_turtle.fillcolor('green')
    
turtle.exitonclick()
