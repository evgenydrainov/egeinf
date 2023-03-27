f=open("17var07.txt")
s=[]
for i in f:
	s.append(int(i))
c=0
mx=-1000000000000
for i in range(len(s)-1):
	if s[i]%3==0 and s[i+1]%3==0:
		c+=1
		mx=max(mx,s[i]+s[i+1])
print(c)
print(mx)