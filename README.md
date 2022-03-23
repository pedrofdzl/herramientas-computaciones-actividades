# Videojuego-Paint 🖌️

## Pedro Andres Fernandez Lopez - A01235998
## José Manuel Saldua González - A00830218

### Funcion circle
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

### Funcion color
```
def color(val):
    tur.color(val)
```
