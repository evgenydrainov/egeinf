for n in range(0,100000):
	r=bin(n)
	r=r[2:]
	r+=r[-1]
	nn=bin(n)
	nn=nn[2:]
	if nn.count("1")%2==0:
		r+="0"
	else:
		r+="1"
	r+=str(r.count("1")%2)
	r=int(r,2)
	if r>80:
		print(r)
		break