import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.title('My Polygon')
the_turtle = turtle.getturtle()

turtle.register_shape('mypoligon',((0,0), (100,0),(140, 40)))

the_turtle.shape('mypoligon')
the_turtle.fillcolor('purple')


for angle in range(0, 360, 10):
    the_turtle.setheading(angle)
    the_turtle.stamp()

turtle.register_shape('mypoligon',((10,0), (10,0),(190, 40)))
for angle in range(0, 360, 10):
    the_turtle.setheading(angle)
    the_turtle.stamp()
    
the_turtle.speed(1)