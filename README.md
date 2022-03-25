# Memorama :brain:

## Pedro Andres Fernandez Lopez - A01235998
## José Manuel Saldua González - A00830218

### Contador de taps (Pedro)
```
# Se crea otra turtle para que esta sea la writer que escribira los textos necesarios
writer = Turtle()
writer.hideturtle()
# Se declaran dos variables globales, startUp para llevar control de si es la primer vez que se itera draw() y nTaps que lleva la cuenta de el numero de taps que ha dado el usuario
startUp = False
nTaps = 0

# (DENTRO DE taps())
# Se lleva un contador global que almacena el numero de taps como entero y lo incrementa en cada llamado de tap()
    global nTaps
    nTaps += 1
    
# (DENTRO DE draw())
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
```

### Funcion nombres (Pedro)
```
# Es llamada dentro de draw en su primera iteracion
def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-190,230)
    writer.color("black")
    writer.write("Jose Saldua A00830218", align="left", font=("chalkboard",10,"normal"))
    writer.goto(-190,210)
    writer.color("black")
    writer.write("Pedro Fernandez A01235998", align="left", font=("chalkboard",10,"normal"))
```

### Winning message (Pedro)
```
# Dentro de draw() se checa si todas las casillas estan reveladas, si es verdad, se muestra el mensaje
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
```
