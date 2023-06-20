alph="POLYGN"
count=0
for a in alph:
	for b in alph:
		for c in alph:
			for d in alph:
				for e in alph:
					if (a == e) and (b == d) and (c in "OY"):
						count+=1
print(count)