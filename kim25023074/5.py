n=1
while True:
	r=bin(n)[2:]
	if len(r)%2==0:
		c=len(r)//2
		r = r[0:c] + "000" + r[c:]
	else:
		r = "1" + r + "01"
	r=int(r,2)
	if r>100:
		print(n)
		break

	n+=1