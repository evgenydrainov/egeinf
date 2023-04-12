print("x y z")
for x in range(2):
	for y in range(2):
		for z in range(2):
			f = ((not(z or x)) or y) and (not x) and ((z and y) <= z)
			if f==1:
				print(x,y,z)