for i in range(999,0,-1):
	a=(i//100)**2 + (i//10%10)**2
	b=(i//10%10)**2 + (i%10)**2
	if b>a:
		c=str(b)+str(a)
	else:
		c=str(a)+str(b)
	if c=="7434":
		print(i,c)
		break