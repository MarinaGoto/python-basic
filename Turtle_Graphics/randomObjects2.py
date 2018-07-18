# Give a set of instructions to create two turtle objects each with circle shape that move to various locations
# of the turtle screen, each stamping their circle shape of varying sizes and colors. 

# Variant 2

import turtle
import random
import time

screen_width = 800
screen_height = 600
buffer = 30

left_boundary = -(screen_width // 2) + buffer
right_boundary = (screen_width // 2) - buffer
top_boundary = (screen_height // 2) - buffer
bottom_boundary = -(screen_height // 2) + buffer

turtle.setup(screen_width, screen_height)
window = turtle.Screen()
window.title('random pattern')
window.colormode(255)

object1 = turtle.Turtle()
object1.hideturtle()
object1.shape('circle')
object1.penup()
object1.resizemode('user')

object2 = turtle.Turtle()
object2.hideturtle()
object2.shape('turtle')
object2.penup()
object2.resizemode('user')

nums_seconds = int(input('How many seconds?:'))

original_time = time.time()

while time.time() - original_time < nums_seconds:    
    for x in (object1, object2):
        x.setposition((random.randint(left_boundary, right_boundary) , 
                        random.randint(bottom_boundary, top_boundary)))
    
        x.turtlesize(random.randint(1, 10), random.randint(1, 10))
    
        x.fillcolor(random.randint(0,255) ,random.randint(0,255) ,random.randint(0,255))
    
        x.stamp()
        
turtle.exitonclick()