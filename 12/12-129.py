s=("8"*9) + ((21-9)*"5")
while "555" in s or "888" in s:
	while "555" in s:
		s=s.replace("555","8",1)
	while "888" in s:
		s=s.replace("888","5",1)
print(s)