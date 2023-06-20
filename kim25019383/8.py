alph="РУСЛАН"
count=0
for a in alph:
	for b in alph:
		for c in alph:
			for d in alph:
				for e in alph:
					s=a+b+c+d+e
					if s.count("У")<=1 and s.count("А")<=1:
						count+=1
print(count)