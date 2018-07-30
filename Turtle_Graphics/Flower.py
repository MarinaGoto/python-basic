import turtle
import random

screen_height = 600
screen_width = 800
buffer = 30

window = turtle.Screen()
window.title('Random walk')
turtle.setup(screen_width, screen_height)




turtle.shape('turtle')
turtle.speed(0)
turtle.goto(0, -200)       #move the turtle to a location (starting point)



count = 0

countUntil = int(input('How many decisions should an object take before reaching the endpoint?  '))



flag = True

while flag: 
    if count < countUntil:
        count += 1
        if (-300 < turtle.xcor() <300) and (-300 < turtle.ycor() < 300):
            turtle.right(random.randint(0,360))
            distance = random.randint(0,100) 
            turtle.forward(distance)
        else:
            turtle.right(180)
            turtle.forward(distance)
            flag = False
    turtle.goto(50, 50)           #move the turtle to a new location
    
turtle.exitonclick()