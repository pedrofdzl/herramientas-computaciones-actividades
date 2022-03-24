from turtle import *
from random import randrange
from freegames import square, vector
from random import randrange, choice

writer = Turtle()
tracer(False)

def info_alumnos():
    color("#000000")
    line(vector(-200,0),vector(200,0))
    line(vector(0,-200),vector(0,200))
    writer.hideturtle()
    writer.up()
    writer.goto(-160,170)
    writer.color("black")
    writer.write("Jose Saldua A00830218", align="left", font=("chalkboard",5,"normal"))
    writer.goto(-160,140)
    writer.color("black")
    writer.write("Pedro Fernandez A01235998", align="left", font=("chalkboard",5,"normal"))
    
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

lista_colores=["black","green","blue","#D6B85A","#82EEFD"]
color_snake = choice(lista_colores)

lista_colores.remove(color_snake)

color_comida = choice(lista_colores)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    rand1 = randrange(0,2)
    rand2 = randrange(0,2)
    if rand1 == 0:
        if rand2 == 0:
            food.x += -10
            if not inside(food):
                food.x += 10
        else:
            food.x += 10
            if not inside(food):
                food.x += -10
    else:
        if rand2 == 0:
            food.y += -10
            if not inside(food):
                food.y += 10
        else:
            food.y += 10
            if not inside(food):
                food.y += -10

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)

def line(p1, p2):
    penup()
    goto(p1)
    pendown()
    goto(p2)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
info_alumnos()
done()
