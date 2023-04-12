f=open("09.csv")
s=[]
for i in f:
	s.append(list(map(int,i.split(";"))))
#print(s)
count=0
for i in range(len(s)):
	j=s[i]
	j.sort()
	rep=[]
	norep=[]
	for k in range(1,len(j)):
		if j[k]==j[k-1]:
			rep.append(j[k])
		else:
			norep.append(j[k])
	if j[0]!=j[1]:
		norep.insert(0,j[0])
	if j[0]==j[1]:
		rep.insert(0,j[0])
	if len(rep)==0: continue
	if len(norep)==0: continue
	print()
	print(j)
	print(rep)
	print(norep)
	if (sum(norep)/len(norep)) > (sum(rep)/len(rep)):
		count+=1
print()
print(count)