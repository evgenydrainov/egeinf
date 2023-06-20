print("x y z w")
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				f= ((w<=z) and ((not x) <= y)) <= ((y==w) or (z and (not x)))
				if f==0:
					print(x,y,z,w)