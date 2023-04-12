n=4
while True:
	s="3"+n*"5"
	b=s
	while "25" in s or "355" in s or "555" in s:
		if "25" in s:
			s=s.replace("25","3",1)
		if "355" in s:
			s=s.replace("355","52",1)
		if "555" in s:
			s=s.replace("555","23",1)
	a=0
	for i in s:
		a+=int(i)
	if a==27:
		print(b)
		print(s)
		print(n)
		exit()
	n+=1