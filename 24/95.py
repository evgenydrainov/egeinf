f=open("24-2.txt")
s=f.readline()
c=1
mx=0
for i in range(len(s)-1):
	if ord(s[i])<ord(s[i+1]):
		c+=1
	else:
		c=1
	mx=max(mx,c)
print(mx)