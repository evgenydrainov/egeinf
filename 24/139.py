f=open("24-s1.txt")
c=0
for i in f:
	if i.count("S")==i.count("X"):
		c+=1
print(c)