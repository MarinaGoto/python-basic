#artistic circles

import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('Drawing a circle')

#get default turtle and hide
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

#shape
the_turtle.shape('turtle')
the_turtle.fillcolor('black')

#color
turtle.colormode(255)
the_turtle.pencolor(16, 171, 19)

#size
the_turtle.pensize(1)

#speed
the_turtle.speed(7)

#create artistic circles 
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    

#wait for user to end
turtle.exitonclick()