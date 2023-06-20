from turtle import *

color("black", "red")
m = 10
speed(10)

left(90)
begin_fill()
for i in range(3):
	forward(10 * m)
	right(120)
end_fill()

cnv=getcanvas()
c=0
for x in range(-100*m, 100*m, m):
	for y in range(-100*m, 100*m, m):
		item=cnv.find_overlapping(x,y,x,y)
		if len(item)==1 and item[0]==5:
			c+=1
print(c)
input()