f=open("27-71a.txt")
s=[]
for i in f:
	s.append(int(i))
mxS=-100000000000000
for i in range(len(s)):
	for j in range(i,len(s)):
		S=0
		for k in range(i,j): S+=s[k]
		if S%69==0:
			if S>=mxS:
				mxS=S
				print("sum ", S, " len ", j-i)