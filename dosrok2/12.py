for n in range(4,10000000):
	s="3"+n*"5"
	while "25" in s or "355" in s or "555" in s:
		if "25" in s:
			s=s.replace("25","32",1)
		if "355" in s:
			s=s.replace("355","25",1)
		if "555" in s:
			s=s.replace("555","3",1)
	a=0
	for i in s:
		a+=int(i)
	if a==17:
		print(n)
		exit()