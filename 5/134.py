res=0
for n in range(124,0,-1):
	r=bin(n)
	r=r[2:]
	if r.count("1")%2==0:
		r+="0"
	else:
		r+="1"
	if r.count("1")%2==0:
		r+="0"
	else:
		r+="1"
	r=int(r,2)
	if r<125:
		res=max(res,r)
print(res)