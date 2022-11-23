for n in range(0,100000):
	r=bin(n)
	r=r[2:]
	r+=r[-1]
	if r.count("1")%2==0:
		r+="0"
	else:
		r+="1"
	if r.count("1")%2==0:
		r+="0"
	else:
		r+="1"
	r=int(r,2)
	if r>114:
		print(r)
		break