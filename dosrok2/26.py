f=open("26.txt")
K=int(f.readline())
N=int(f.readline())
s=[]
for i in f:
	sp=i.split(" ")
	s.append([int(sp[0]), int(sp[1])])
slot=[0]*K
s.sort()
c=0
for i in range(len(s)):
	st=s[i][0]
	end=s[i][1]
	klal=0
	for j in range(K):
		if slot[j]<st:
			slot[j]=end
			klal=1
			break
	if klal:
		c+=1
print(c)
	
