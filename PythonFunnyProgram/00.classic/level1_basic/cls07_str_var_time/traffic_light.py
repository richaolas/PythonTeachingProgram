from turtle import*
import time
shape('turtle')
penup()
fillcolor('black')
begin_fill()
goto(-50, -100)
pendown()
left(90)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(100)
end_fill()
penup()
goto(0,0)
setheading(0)
left(90)
forward(50)
right(180)
dot(50,'red')
time.sleep(6)
dot(50,'#f99078')
forward(50)
dot(50,'yellow')
time.sleep(6)
dot(50,'#E3F97A')
forward(50)
dot(50,'green')
time.sleep(6)
dot(50,'#82F97A')
done()