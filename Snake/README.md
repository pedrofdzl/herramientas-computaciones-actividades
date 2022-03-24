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
