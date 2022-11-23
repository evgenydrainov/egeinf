for i in range(81, 1000000):
	s="1"*i
	while "111" in s:
		s=s.replace("111","2",1)
		s=s.replace("222","1",1)
	if s=="21":
		print(i)
		break