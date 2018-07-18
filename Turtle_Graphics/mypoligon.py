# Give a set of instructions to create your own polygon shape and create an interesting design with it. 

# 1st row of colored arrows
import turtle

turtle.setup(800, 600)
window = turtle.Screen()
window.title('My Polygon')
the_turtle = turtle.getturtle()
the_turtle.resizemode('user')
turtle.register_shape('mypoligon',((0,0), (100,0),(140, 40)))
the_turtle.speed(9)


x_position = 0
y_position = 0
turtle_size = 10
while y_position < 250:
    the_turtle.setposition(x_position, y_position)
    the_turtle.turtlesize(turtle_size, turtle_size)
    the_turtle.stamp()
    x_position = x_position + 50
    y_position = y_position + 50
    turtle_size = turtle_size - 2
    if x_position < 75:
        the_turtle.fillcolor('blue')
    elif x_position == 75 or x_position < 100:
        the_turtle.fillcolor('red')
    elif x_position == 100 or x_position < 150:
        the_turtle.fillcolor('green')
    elif x_position == 150 or x_position < 200:
        the_turtle.fillcolor('yellow')
    elif x_position == 200 or x_position < 250:
        the_turtle.fillcolor('black')
    else:
        the_turtle.fillcolor('pink')
turtle.exitonclick()



# 2st PYTHON


#incrice in loop 

import turtle
turtle.setup(800, 600)
window = turtle.Screen()
window.title('My Polygon')
the_turtle = turtle.getturtle()
the_turtle.resizemode('user')
turtle.register_shape('mypoligon',((0,0), (100,0),(140, 40)))
the_turtle.speed(6)


x_position = -350
y_position = 250
turtle_size = 5
turtle.colormode(255)
the_turtle.penup()
while x_position < 350:
    the_turtle.setposition(x_position, y_position)
    the_turtle.pendown()
    the_turtle.turtlesize(turtle_size, turtle_size)
    the_turtle.stamp()
    x_position = x_position + 30
  #  y_position = y_position + 1
  #  turtle_size = turtle_size - 2
    
    if x_position < 30:       
        the_turtle.fillcolor(153, 0, 204)
    elif x_position == 30 or x_position < 80:        
        the_turtle.fillcolor(172, 0, 230)
    elif x_position == 80 or x_position < 115:       
        the_turtle.fillcolor(198, 26, 255)
    elif x_position == 115 or x_position < 130:       
        the_turtle.fillcolor(210, 77, 255)
    elif x_position == 145 or x_position < 200:     
        the_turtle.fillcolor(223, 128, 255)
    else:   
        the_turtle.fillcolor(236, 179, 255)
        
##PYTHON
the_turtle.hideturtle()
#shape
the_turtle.shape('turtle')
the_turtle.fillcolor('black')
#color
turtle.colormode(255)
the_turtle.pencolor(169, 17, 169)
#size
the_turtle.pensize(4)

#create python

# P
the_turtle.penup()
the_turtle.setposition(-300, -200)
the_turtle.pendown()
the_turtle.setposition(-300, 200)
the_turtle.pendown()
the_turtle.setposition(-250, 200)
the_turtle.pendown()
the_turtle.setposition(-250,100)
the_turtle.pendown()
the_turtle.setposition(-300,100)

#Y
the_turtle.penup()
the_turtle.setposition(-200, 200)
the_turtle.pendown()
the_turtle.setposition(-200, 100)
the_turtle.pendown()
the_turtle.setposition(-150, 100)
the_turtle.pendown()
the_turtle.setposition(-150,200)
the_turtle.pendown()
the_turtle.setposition(-150,-200)
the_turtle.pendown()

#T
the_turtle.penup()
the_turtle.setposition(-50, -200)
the_turtle.pendown()
the_turtle.setposition(-50, 200)
the_turtle.pendown()
the_turtle.setposition(-100, 200)
the_turtle.pendown()
the_turtle.setposition(0,200)

#H
the_turtle.penup()
the_turtle.setposition(50, 200)
the_turtle.pendown()
the_turtle.setposition(50, -200)
the_turtle.pendown()
the_turtle.setposition(50, 0)
the_turtle.pendown()
the_turtle.setposition(150,0)
the_turtle.pendown()
the_turtle.setposition(150, 200)
the_turtle.pendown()
the_turtle.setposition(150,-200)

#O
the_turtle.penup()
the_turtle.setposition(200, -200)
the_turtle.pendown()
the_turtle.setposition(200, 200)
the_turtle.pendown()
the_turtle.setposition(250, 200)
the_turtle.pendown()
the_turtle.setposition(250,-200)
the_turtle.pendown()
the_turtle.setposition(200, -200)

#N
the_turtle.penup()
the_turtle.setposition(300, -200)
the_turtle.pendown()
the_turtle.setposition(300, 200)
the_turtle.pendown()
the_turtle.setposition(350, -200)
the_turtle.pendown()
the_turtle.setposition(350,200)





turtle.exitonclick()

