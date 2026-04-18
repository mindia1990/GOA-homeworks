from turtle import*

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drowing a dor

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of thr door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(80, 140)
pendown()

#drowing leftside window

color("blue")
begin_fill()
right(60)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()

penup()
goto(120,140)
pendown()

#drowing rightside window
color("blue")
begin_fill()
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()


exitonclick()





