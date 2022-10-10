for i in range(222987, 223021+1):
	s = []
	for j in range(1, i//2 + 1):
		if i%j == 0:
			s.append(j)
	s.append(i)
	if len(s)==4:
		print(s)