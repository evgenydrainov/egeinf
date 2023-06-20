from turtle import *
color("black", "red")
left(90)
speed(100)
m=1000
begin_fill()
right(225)
for i in range(6):
	forward(15*m)
	right(60)
	forward(7*m)
	right(120)
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