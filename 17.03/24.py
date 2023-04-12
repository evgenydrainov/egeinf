f=open("24var05-08.txt")
s=f.readline()
a=""
mx=-100000000
for i in range(len(s)):
	a+=s[i]
	if len(a)>3:
		if a[-4:-1] == "000":
			a="00"
	mx=max(mx,len(a))
print(mx)