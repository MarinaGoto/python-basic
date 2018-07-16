#  Give a set of instructions for controlling the turtle to create three concentric circles, 
# each of different color and line width. 

import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing tree circles')

#get default turtle and hide
the_turtle = turtle.getturtle()
#the_turtle.hideturtle()

#1 circle
the_turtle.resizemode('user')
the_turtle.turtlesize(3,3)
the_turtle.shape('circle')
the_turtle.fillcolor('blue')
the_turtle.stamp()

#2 circle
the_turtle.resizemode('user')
the_turtle.turtlesize(2,2)
the_turtle.shape('circle')
the_turtle.fillcolor('green')
the_turtle.stamp()

#3 circle
the_turtle.resizemode('user')
the_turtle.turtlesize(1,1)
the_turtle.shape('circle')
the_turtle.fillcolor('white')
the_turtle.stamp()

#size
the_turtle.pensize(50)

#speed
the_turtle.speed(7)

    

#wait for user to end
turtle.exitonclick()