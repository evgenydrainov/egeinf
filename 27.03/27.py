f=open("27v07_A.txt")
s=[]
for i in f:
	s.append(int(i))
mx=-10000000000
for i in range(0,len(s)):
	for j in range(i,len(s)):
		a=0
		for k in range(i,j): a+=s[k]
		if a%145==0:
			if a>=mx:
				mx=a
				print("max sum ", a, " from i ", i, " to j ", j, " count ", j-i, mx/145)
