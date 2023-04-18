for i in range(1200108,10**8+1,273):
	s=str(i)
	if s[0:0+2]=="12" and s[4:4+2]=="36" and s[-1]=="1":
		print(i, i//273)