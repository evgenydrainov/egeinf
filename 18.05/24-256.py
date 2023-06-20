f=open("24-256.txt")
s=f.readline()
c=2
mx=-10000
for i in range(2,len(s)):
	c+=1
	if (s[i-2] in "NOT") and (s[i] in "NOT"):
		c=2
	mx=max(mx,c)
print(mx)