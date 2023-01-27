for a in range(1,100000):
	f=1
	for x in range(1,100000):
		if ( (x % 18 != 0) <= ((x % a != 0) <= (x % 12 != 0)) ) == 0:
			f=0
	if f==1:
		print(a)