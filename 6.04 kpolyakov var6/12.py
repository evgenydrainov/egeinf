for n in range(100,201):
	for m in range(100,201):
		for k in range(100,201):
			s = ">" + k * "1" + m * "2" + n * "*"
			while (">1" in s) or (">2" in s) or (">*" in s):
				if ">1" in s:
					s=s.replace(">1","111>",1)
				if ">2" in s:
					s=s.replace(">2","1>",1)
				if ">*" in s:
					s=s.replace(">*","%2*>")
			S=0
			for i in s:
				if i!="%" and i!="*" and i!=">": S+=int(i)
			if S==1190:
				print(n,k,m)
				exit()