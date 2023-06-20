n=1
while True:
	r=bin(2*n)[2:]

	r+=str(bin(n)[2:].count("1")%2)
	#r+=str(r.count("1")%2) ?

	r+=str(r.count("1")%2)
	if int(r,2)>249:
		print(n)
		break
	n+=1