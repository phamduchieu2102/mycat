#coding=utf-8
import turtle
import time
t = turtle.Turtle()
#vẽ đầu
t.fillcolor("pink")
t.begin_fill()
i = 0
while i < 4:
    t.fd(100)
    t.lt(90)
    i += 1
t.end_fill()
#vẽ thân
t.penup()
t.goto(100, 50)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
for i in range(4):
    t.fd(150)
    t.rt(90)
t.end_fill()
#vẽ đuôi
t.penup()
t.goto(250, 11)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.rt(45)
t.fd(80)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(70)
t.end_fill()
#vẽ mắt
t.pu()
t.goto(78, 68)
t.pd()
t.lt(45)
t.fillcolor("blue")
t.begin_fill()
i = 0
while i < 4:
    t.fd(15)
    t.lt(90)
    i += 1
t.end_fill()
t.pu()
t.goto(36, 67)
t.pd()
t.fillcolor("blue")
t.begin_fill()
i = 0
while i < 4:
    t.fd(15)
    t.lt(90)
    i += 1
t.end_fill()
#vẽ chân
t.pu()
t.goto(129, -101)
t.pd()
t.lt(90)
t.fillcolor("yellow")
t.begin_fill()
i = 0
while i < 3:
    t.fd(30)
    t.lt(90)
    i += 1
t.end_fill()
t.pu()
t.goto(226, -101)
t.pd()
t.lt(90)
t.fillcolor("yellow")
t.begin_fill()
i = 0
while i < 3:
    t.fd(30)
    t.rt(90)
    i += 1
t.end_fill()
t.pu()
t.goto(79, 100)
t.pd()
#vẽ tai
t.fillcolor("brown")        
t.begin_fill()
t.goto(70, 119)
t.goto(63, 100)
t.goto(37, 100)
t.goto(28, 119)
t.goto(20, 101)
t.end_fill()
#vẽ mồm
t.pu()
t.goto(80, 33)
t.pd()
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(5)
def get_mouse_click_coor(x, y): #đoạn code này cần để ở vị trí dưới cùng; 
  print(x, y) #câu lệnh này 
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() 



