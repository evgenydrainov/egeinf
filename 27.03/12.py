s=50*"1"
while "11111" in s or "15" in s:
	if "11111" in s:
		s=s.replace("11111","15",1)
	else:
		s=s.replace("15","1",1)
print(s)