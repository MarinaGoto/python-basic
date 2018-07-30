# A random walk is a trajectory taken by a sequence of random steps. Random walks
# can be used to model the travel of molecules, the path that animals take when looking
# for food, and the path a lost man takes to find his way home, etc.


import turtle
import random

screen_height = 600
screen_width = 800

turtle.setup(screen_width,screen_height)
window = turtle.Screen()
window.title('Random walk')



cosmos = turtle.Turtle()
turtle.register_shape('cosmos.gif')
cosmos.shape('cosmos.gif')


turtle1 = turtle.Turtle()
turtle.register_shape('Cosmonaut.gif')
turtle1.shape('Cosmonaut.gif')
turtle1.goto(-1, -160)
turtle1.pencolor('white')

#test = turtle.Turtle()
#turtle.register_shape('planet.gif')
#test.shape('planet.gif')
#test.goto(200, -130)

#end = turtle.Turtle()
#turtle.register_shape('end.gif')
#end.shape('end.gif')
#end.goto(-220, -240) # endpoint test


endPoint = int(input('What planet shall the austranavt land on? \n Orange planet right top: 1  \n Orange small planet top center: 2 \n Grey planet bottom right: 3 \n Blue small planet center: 4 \n Green planet bottom: 5 \n ANSWER: '))
if endPoint == 1:
    endA = 290
    endB = 215
elif endPoint == 2:
    endA = -70
    endB = 215
elif endPoint == 3:
    endA = 200
    endB = -130
elif endPoint == 4:    
    endA = -50
    endB = -80 
else:
    endA = -220
    endB = -240 


# 3) Allow users to select if the walking path of the lost man should be presented on the window or not.

penChoice = input('Do you want to see the walking path?  (y/n)')
if penChoice == 'n':
    turtle1.penup()
else:
    turtle1.pendown()     


# 1.1) allow users to input a number of times the man
# should make a decision for his walking direction. An input number 5 means the man will
# walk five city blocks. 

count = 0
countUntil = int(input('How many decisions should an object take before reaching the endpoint?  '))



# 2) Allow users to specify how fast the man walk.

speedChoice = int(input('How fast the object walk? (0,10)  '))
turtle1.speed(speedChoice)

distance = random.randint(10,30)
    
flag = True

while flag : 
    if count < countUntil:
        count += 1
        print(round(turtle1.position()[0]))   # check x position 
        if (((-535 < round(turtle1.position()[0]) < -20)) and (-180 < round(turtle1.position()[1]) < 235 ))  or (((-290 < round(turtle1.position()[0]) < -150)) and (-170 < round(turtle1.position()[1]) < -310 )) or (((-120 < round(turtle1.position()[0]) < 20)) and (-150 < round(turtle1.position()[1]) < -10 )) or (((-90 < round(turtle1.position()[0]) < 90)) and (-160 < round(turtle1.position()[1]) < 160 )) or (((195 < round(turtle1.position()[0]) < 385)) and (122 < round(turtle1.position()[1]) < 312 )) or (((70 < round(turtle1.position()[0]) < 330)) and (-260 < round(turtle1.position()[1]) < 0 )) or  (((100 < round(turtle1.position()[0]) < 320)) and (-240 < round(turtle1.position()[1]) < -10 )) or not ((-340 < round(turtle1.position()[0]) < 340) and (-280 < round(turtle1.position()[1]) < 240)):
            print('turn back')
            turtle1.right(180)
            turtle1.forward(distance)
        else:
            print('safe case')
            turtle1.setheading(random.randint(0,360))        
            turtle1.forward(distance)

    else:  
        turtle1.goto(endA, endB)           # move the turtle to a new location    (endpoint!!)  
        flag = False
        


############################################################  

       
turtle.exitonclick()
