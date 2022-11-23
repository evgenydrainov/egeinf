for n in range(0, 100000):
	s=bin(n)
	s=s[2:]
	if s.count("1")%2==0:
		s+="1"
	else:
		s+="0"
	if s.count("1")%2==0:
		s+="1"
	else:
		s+="0"
	r=int(s,2)
	if r>54:
		print(r)
		break