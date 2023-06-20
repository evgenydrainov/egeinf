from turtle import *
color("black", "red")
left(90)
begin_fill()
right(315)
speed(100)
m=1000
for i in range(2):
    forward(12*m)
    right(45)
    forward(6*m)
    right(135)
end_fill()
cnv=getcanvas()
count=0
for y in range(-100*m, 100*m, m):
    for x in range(-100*m, 100*m, m):
        i=cnv.find_overlapping(x, y, x, y)
        if len(i)==1 and i[0]==5:
            count+=1
print(count)
done()