from turtle import * 

#we want to paint a house

#step1:draw a square
speed(30)
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

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
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
#making windows
left(30)
penup()
forward(70)
left(90)
forward(70)
pendown()
color("blue")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#draw a window 2
penup()
forward(60)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#draw a sun
penup()
left(90)
forward(150)
left(90)
forward(200)
pendown()
color("yellow")
begin_fill()
circle(50)
end_fill()

exitonclick()