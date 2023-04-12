for A in range(1000000):
	fl=0
	for x in range(100000):
		f = ((x&39)==0) or (((x&11)==0) <= ((x&A)!=0))
		if f==0:
			fl=1
			break
	if fl==0:
		print(A)
		exit()