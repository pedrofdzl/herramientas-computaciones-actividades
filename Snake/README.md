# Snake-Game :snake:

## Pedro Andres Fernandez Lopez - A01235998
## José Manuel Saldua González - A00830218



### Funcion info Alumnos (Jose Manuel)
```
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
```
### color comida/snake (Jose Manuel)
```
lista_colores=["black","green","blue","#D6B85A","#82EEFD" ]
color_snake = choice(lista_colores)

lista_colores.remove(color_snake)

color_comida = choice(lista_colores)
```
### Movimiento al azar de la comida dentro de move() (Pedro)
```
    global foodCounter
    if(foodCounter == 3):
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
        foodCounter = 0
    else:
        foodCounter += 1
```

### Validacion del spawn de la comida (Pedro)
```
while food in snake:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
```

### Score del jugador (extra) (Pedro)
```
def refresh_score():
    color("#000000")
    writer.hideturtle()
    writer.up()
    writer.goto(160,170)
    writer.color("white")
    writer.begin_fill()
    writer.circle(10)
    writer.end_fill()
    writer.color("black")
    writer.write(len(snake), align="left", font=("chalkboard",10,"normal"))
```

## Gif del funcionamiento
![Gif](https://imgur.com/a/decRjTN)
