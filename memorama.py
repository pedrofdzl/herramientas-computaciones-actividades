from random import *
from turtle import *
from freegames import path

# Se crea otra turtle para que esta sea la writer que escribira los textos necesarios
writer = Turtle()
writer.hideturtle()
# Se declaran dos variables globales, startUp para llevar control de si es la primer vez que se itera draw() y nTaps que lleva la cuenta de el numero de taps que ha dado el usuario
startUp = False
nTaps = 0

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-190,230)
    writer.color("black")
    writer.write("Jose Saldua A00830218", align="left", font=("chalkboard",10,"normal"))
    writer.goto(-190,210)
    writer.color("black")
    writer.write("Pedro Fernandez A01235998", align="left", font=("chalkboard",10,"normal"))

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    # Se lleva un contador global que almacena el numero de taps como entero y lo incrementa en cada llamado de tap()
    global nTaps
    nTaps += 1
    
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Variable que lleva el control de cuantos cuadros siguen ocultos
    hidden = 0
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            hidden += 1

    if(hidden == 0):
        writer.up()
        writer.color("black")
        writer.goto(0,-10)
        writer.write("Ganaste un auto!!!", align="center", font=("chalkboard",20,"normal"))
        writer.goto(0, 10)
        writer.write("Felicidades!!", align="center", font=("chalkboard",20,"normal"))


    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    
    # Se dibuja el numero de taps y los nombres
    global nTaps
    global startUp
    writer.up()
    writer.goto(200, 210)
    writer.color("white")
    writer.begin_fill()
    writer.circle(10)
    writer.end_fill()
    writer.up()
    writer.goto(160, 210)
    writer.color("black")
    if(not startUp):
        # Si el la primera vez que se itera draw() se dibuja el texto y los nombres
        writer.write("Taps: "+str(nTaps), align="left", font=("chalkboard",10,"normal"))
        info_alumnos()
        startUp = True
    else:
        writer.goto(200, 210)
        writer.write(str(nTaps), align="left", font=("chalkboard",10,"normal"))

    if(hidden > 0):
        ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
