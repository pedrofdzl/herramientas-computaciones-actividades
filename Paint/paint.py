#Jose Manuel Saldua A00830218
#Pedro Andres Fernandez Lopez A01235998
from turtle import *
from freegames import vector
from math import *
import turtle as tur

writer = Turtle()

def info_alumnos():
    color("#000000")
    line(vector(-200,0),vector(200,0))
    line(vector(0,-200),vector(0,200))
    writer.hideturtle()
    writer.up()
    writer.goto(-160,170)
    writer.color("black")
    writer.write("Jose Saldua A00830218", align="left", font=("chalkboard",15,"normal"))
    writer.goto(-160,140)
    writer.color("black")
    writer.write("Pedro Fernandez A01235998", align="left", font=("chalkboard",15,"normal"))
    

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end): #Funcion para crear un Circulo
    "Draw circle from start to end."
    midX = 0
    midY = 0
    if(start.x < end.x):
        midX = start.x - end.x
    else:
        midX = end.x - start.x
    if(start.y < end.y):
        midY = start.y - end.y
    else:
        midY = end.y - start.y
            
    up()
    goto(midX, midY)
    down()

    rad = sqrt(pow(abs(start.x - midX), 2) + pow(abs(start.y - midY), 2))/2

    tur.circle(rad)
    
    pass  # TODO

def rectangle(start, end): #Funcion para crear un Rectangulo
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.x - start.x*2)
        left(90)
        

    end_fill()
    pass  # TODO

def triangle(start, end): #Funcion para crear un Triangulo
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(60)
        
    end_fill()
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value
    
def color(val):
    tur.color(val)

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
