print("x y z w")
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				f=((x<=y)<=z)or(w<=(y and z))
				if f==0:
					print(x,y,z,w)