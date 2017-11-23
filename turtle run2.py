import turtle as t
import math

t.speed(0)

x_min=-5
x_max=+5

y_min=-5
y_max=+5

space=0.01

t.setworldcoordinates(x_min,y_min,x_max,y_max)

t.up()
t.goto(x_min,0)
t.down()
t.goto(x_max,0)
t.up()
t.goto(0,y_min)
t.down()
t.goto(0,y_max)

t.color("red")

func=input("?")

x=x_min
exec(func)
t.up()
t.goto(x,y)
t.down()
while x<=x_max:
    x=x+space
    exec(func)
    t.goto(x,y)

func2=input("?")

t.color("blue")

x=x_min
exec(func2)
t.up()
t.goto(x,y)
t.down()
while x<=x_max:
    x=x+space
    exec(func2)
    t.goto(x,y)

list1=[]

list1.append(


#func 두개를 입력받고, 리스트를 하나씩 만든다.
#두 리스트를 비교해서 두 x 의 결과값의 거리가 일정 이하보다 작으면 동일한 값으로 추정
#http://blog.naver.com/jinp7/220934924630             
