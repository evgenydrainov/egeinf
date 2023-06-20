for A in range(0,100000000):
	f=0
	for x in range(1000):
		for y in range(1000):
			F=(x>=9)or(2*x<y)or(x*y<A)
			if F==0:
				f=1
				break
		if f==1: break
	if f==0:
		print(A)
		exit()