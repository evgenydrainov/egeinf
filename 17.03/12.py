s=2022*"1"
while "11" in s or "555" in s:
	if "11" in s:
		s=s.replace("11","555",1)
	else:
		s=s.replace("555","5",1)
print(s)