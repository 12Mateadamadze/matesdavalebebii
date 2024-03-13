from turtle import *

#we want to paint a house

#step 1: draw a square

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

#draw a door

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

penup() 
goto(140, 140) 
pendown()

right(150) 
color("blue") 
forward(36) 
right(90) 
forward(36) 
right(90) 
forward(36) 
right(90) 
forward(36) 
right(180) 
forward(18) 
left(90) 
forward(35)

penup() 
goto(10, 140)
pendown()

right(90) 
color("blue") 
forward(36) 
left(90) 
forward(36) 
left(90) 
forward(36) 
left(90) 
forward(36) 
left(90) 
forward(18) 
left(90) 
forward(36)

exitonclick() 