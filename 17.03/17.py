f=open("17var06.txt")
s=[]
for i in f:
	s.append(int(i))
c=0
mn=10000000000000000
for i in range(len(s)-1):
	if (s[i]>0 and int(s[i]**0.5)**2 == s[i]) or (s[i+1]>0 and int(s[i+1]**0.5)**2 == s[i+1]):
		c+=1
		mn=min(mn,s[i]+s[i+1])
print(c)
print(mn)
