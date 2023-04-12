c=0
for n in range(1,1001):
#for n in range(5,6):
	r=bin(n)[2:]
	if r.count("1")%2==0:
		r=r[1:]
	else:
		r=r.replace("0","")
		r+="1"
	if r.count("1")%2==0:
		r=r[1:]
	else:
		r=r.replace("0","")
		r+="1"
	r=int(r,2)
	if r==7:
		c+=1
print(c)