for n in range(0,100000):
	s=bin(n)
	s=s[2:]
	if s.count("1")%2==0:
		s+="0"
	else:
		s+="1"
	if s.count("1")%2==0:
		s+="0"
	else:
		s+="1"
	r=int(s,2)
	if r>184:
		print(n)
		break;