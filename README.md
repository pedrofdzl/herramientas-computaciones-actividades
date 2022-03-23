# videojuego-paint
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
