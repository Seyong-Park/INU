import turtle as t # turtle 출력, t라고 부른다.
t.shape("turtle") # shape을 turtle로 한다.

n=9
t.color("purple") # 펜 색상을 보라색으로 바꿈
t.pensize(1.5) # 펜 굵기를 1.5로 바꿈
t.begin_fill()
for x in range(n): # n번만큼 반복한다.
    t.forward(50)
    t.left(360/n)
t.end_fill()
