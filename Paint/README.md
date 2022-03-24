# Videojuego-Paint 🖌️

## Pedro Andres Fernandez Lopez - A01235998
## José Manuel Saldua González - A00830218

### Funcion circle (Pedro)
```
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
```

### Funcion color (Pedro)
```
def color(val):
    tur.color(val)
```

### Funcion alumnos (Jose Manuel)
```
def info_alumnos(): #Jose Manuel Saldua
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
 
 ### Funcion rectangle (Jose Manuel)
 ```
 def rectangle(start, end): #Jose Manuel Saldua
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
```

### Funcion triangle (Jose Manuel)
```
def triangle(start, end): #Jose Manuel Saldua
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(60)
        
    end_fill()
    pass  # TODO
```
![Gif](https://gifyu.com/image/SpvWK)
