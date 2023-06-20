f=open("24.txt")
s=f.readline()
c=1
mx=-1000000
for i in range(1, len(s)):
	c+=1
	if (s[i] in "QRS") and (s[i-1] in "QRS"):
		c=1
	mx=max(mx,c)
print(mx)