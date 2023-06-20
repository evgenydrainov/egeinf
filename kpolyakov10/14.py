for x in range(15):
	for y in range(17):
		n= 5 + x*15 + 3*15**2 + 2*15**3 + 1*15**4
		n+=9 + y*17 + 7*17**2 + 6*17**3
		if n%131==0:
			print("x", x, "y", y, ": ", n/131)