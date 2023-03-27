#319
alph="АЛМОС"
for a in alph:
	for b in alph:
		for c in alph:
			for d in alph:
				for e in alph:
					s=a+b+c+d+e
					if s.count("А")<=1 and s.count("М")==2 and not ("Л" in s):
						print(s)
						exit()