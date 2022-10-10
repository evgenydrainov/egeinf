for i in range(190061, 190081):
	s = []
	for j in range(1, i // 2 + 1):
		if i%j==0:
			if j%2!=0:
				s.append(j)
	if i%2!=0:
		s.append(i)
	if len(s)==4:
		s=s[::-1]
		print(s)