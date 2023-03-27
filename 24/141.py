import re
f=open("24-s1.txt")
c=0
for i in f:
	s=re.findall("F.O",i)
	#print(s)
	#if len(s)==0: input()
	if len(s)>0: c+=1
print(c)