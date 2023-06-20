for x in range(17):
	n = 0 + x*17 + 0*17**2 + 1*17**3
	n+= 15 + 15*17 + x*17**2 + 0 + 15*17**4
	if n%13==0:
		print(x, n/13)
		break