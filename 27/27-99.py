f=open("27-99a.txt")
N = int(f.readline())
s=[]
for i in f:
	s.append(int(i))
print(N)
print(len(s))
print(s)
mincost=10000000000000
for st in range(N):
	#print("START ",st)
	cost=0
	for i in range(N):
		ind=(st+i)%N
		#print("IND ",ind,end=" ")
		dist=min(abs(st-ind), abs(ind-(st-N)), abs(st+N-ind))
		cost+=s[ind]*dist
		#print("DIST",dist,end=" ")
	#print()
	#print("COST ",cost)
	if cost<=mincost:
		mincost=cost
		print("COST ",cost," START ",st," ANS ",st+1)
#print()
#print(mincost)