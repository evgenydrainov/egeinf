f=open("17.txt")
s=[]
for i in f:
	s.append(int(i))

mean=0
for i in s:
	mean += i
mean /= len(s)

count=0
mx=-1000000000000000
for i in range(len(s)-2):
	if s[i]<mean or s[i+1]<mean or s[i+2]<mean:
		if "9" in str(s[i]) and "9" in str(s[i+1]) and "9" in str(s[i+2]):
			count += 1
			mx=max(mx, s[i]+s[i+1]+s[i+2])
print(count)
print(mx)