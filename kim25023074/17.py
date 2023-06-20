f=open("17.txt")
s=[]
for i in f:
	s.append(int(i))
c=0
for i in range(len(s)):
	if s[i]%5==0:
		c+=1
count=0
mx=-10000000
for i in range(len(s)-1):
	if (s[i]<0 and s[i+1]>=0) or (s[i+1]<0 and s[i]>=0):
		if (s[i] + s[i+1]) < c:
			count+=1
			mx=max(mx, s[i] + s[i+1])
print(count, mx)