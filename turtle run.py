import turtle as t
import random


te=t.Turtle()
te.shape("turtle")
te.color("red")
te.up()

ts=t.Turtle()
ts.shape("circle")
ts.color("green")
ts.up()
ts.speed(0)

t.bgcolor("orange")

t.shape("turtle")
t.up()
t.fd(250)
t.down()
t.rt(90)
t.fd(250)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(250)
t.up()
t.home()
t.color("white")

te.goto(0,200)
ts.goto(0,-200)
t.goto(0,100)
t.write("Turtle Run",False,"center",("",15))
t.home()

def turn_up():
    t.seth(90)

def turn_down():
    t.seth(270)

def turn_right():
    t.seth(0)

def turn_left():
    t.seth(180)

def play():
    t.fd(4)
    ang=te.towards(t.pos())
    te.seth(ang)
    te.fd(3)

    
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.listen()

s=0
while True:
    play()
    if t.distance(te)<20:
        print("잡혔다!")
        t.write("Game Over"+str(s)+"점",False,"center",("",20))
        while True==x:
            x=False
    if t.distance(ts)<20:
        s=s+1
        print("먹었다!")
        tsx=random.randint(-230,230)
        tsy=random.randint(-230,230)
        ts.goto(tsx,tsy)        
