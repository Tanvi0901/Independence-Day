from turtle import*
from random import randint
import winsound
import random
speed('fastest')
setup(1000,700)
bgcolor("black")
#PLAYING SONG
winsound.PlaySound("WhatsApp Audio 2021-08-14 at 10.12.02 PM.wav",winsound.SND_ASYNC)
#STAR
def star():
    for i in range(5):
        for colours in ["orange","white","green"]:
            pensize(2)
            color(colours)
            begin_fill()
            forward(20)
            right(144)
        end_fill()
x=-650
y=330
for i in range(25):
    penup()
    goto(x,y)
    pendown()
    star()
    x+=50
hideturtle()
# #FLAG
penup()
goto(-250,170)
pendown()
color("orange")
begin_fill()
for i in range(2):
    forward(500)
    right(90)
    forward(100)
    right(90)
end_fill()
right(90)
forward(100)
color("white")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(500)
    left(90)
end_fill()
forward(100)
color("darkgreen")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(500)
    left(90)
end_fill()
penup()
goto(-60,20)
pendown()
color("blue")
begin_fill()
circle(70)
end_fill()
penup()
goto(-50,20)
pendown()
color("white")
begin_fill()
circle(60)
end_fill()
penup()
goto(-20,20)
pendown()
color("blue")
begin_fill()
circle(30)
end_fill()
penup()
goto(67,29)
pendown()
color("navy")
for i in range(24):
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(15)
    right(15)
    pendown()
penup()
goto(10,20)
pendown()
pensize(3)
for i in range(24):
    forward(60)
    backward(60)
    left(15)
#
def spiro():
    for i in range(20):
        for colours in ["orange","white","green"]:
            color(colours)
            left(12)
            forward(70)
            left(90)
x=-350
for i in range(2):
    penup()
    goto(x,-200)
    pendown()
    pensize(1)
    spiro()
    x+=650
penup()
goto(500,120)
pendown()
color("orange")
for i in range(36):
    forward(100)
    backward(100)
    left(10)
penup()
goto(500,0)
pendown()
color("white")
for i in range(36):
    forward(100)
    backward(100)
    left(10)
penup()
goto(500,0)
pendown()
color("blue")
for i in range(36):
    forward(60)
    backward(60)
    left(10)
penup()
goto(500,-120)
pendown()
color("darkgreen")
for i in range(36):
    forward(100)
    backward(100)
    left(10)
penup()
goto(-250,-250)
pendown()
pensize(3)
color("orange")
write("HAPPY",font=("Arial",30,"bold"))
hideturtle()
##pip install pywin32
from win32com.client import Dispatch
def speak(str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.speak(str)
if __name__=='__main__':
    speak("HAPPY")
penup()
goto(-110,-270)
pendown()
color("white")
write("INDEPENDENCE",font=("Arial",30,"bold"))
if __name__=='__main__':
    speak("INDEPENDENCE")
penup()
goto(150,-320)
pendown()
color("green")
write("DAY",font=("Arial",30,"bold"))
if __name__=='__main__':
    speak("DAY")
w=Screen()
w.addshape("pic.gif")
m=Turtle()
m.speed(3)
m.shape("pic.gif")
m.clear
m.goto(-550,0)
x=-400
y=-400
for i in range(18):
    penup()
    goto(x,y)
    pendown()
    star()
    x+=50

hideturtle()
exitonclick()
