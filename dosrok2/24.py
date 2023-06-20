f=open("24.txt")
s=f.readline()
c=1
mx=-100000000
for i in range(1,len(s)):
	c+=1
	if s[i] in "XYZ" and s[i+1] in "XYZ":
		c=1
	mx=max(mx,c)
print(mx)