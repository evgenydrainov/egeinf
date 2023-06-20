f=open("24.txt")
s=f.readline()
count=3
mx=-1000
for i in range(3, len(s)):
	count+=1
	if (s[i-3] in "CDF") and (s[i-2] in "AO") and (s[i-1] in "AO") and (s[i] in "CDF"):
		count=3
	mx=max(mx,count)
print(mx)