c=0
for i in range(1000000,9999999+1):
#for i in range(1234567,1234567+1):
	s=str(i)
	_2to3 = s[1:3]
	kvadr=str(int(s[0])**2)
	if len(kvadr)<2: kvadr="0"+kvadr
	kyb=str(int(s[6])**3)
	_4to6 = s[3:3+3]
	last=_4to6[3-len(kyb):3]
	if _2to3==kvadr and last==kyb:
		c+=1
	#print("2to3", _2to3, "kvadr", kvadr, "4to6last", last, "kyb", kyb)
print(c)