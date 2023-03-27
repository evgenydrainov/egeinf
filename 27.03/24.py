f=open("24var05-08.txt")
s=f.readline()
print(len(s))
c=1
mx=-10
for i in range(1,len(s)):
	c+=1
	if s[i-1:i+1]=="12" or s[i-1:i+1]=="21":
		c=1
	mx=max(mx,c)
print(mx)