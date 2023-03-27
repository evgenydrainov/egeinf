n=2*3**2022 + 5*3**1800 + 3**1001 + 4*3**1000 + 3
c=0
s=""
while n>0:
	if n%9==0:
		c+=1
	s=str(n%9)+s
	n//=9
print(s)
print(c)