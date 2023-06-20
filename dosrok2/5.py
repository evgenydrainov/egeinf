#s="123456789"
#print(s[-3:])

for n in range(4,1000000000):
	r=bin(n)[2:]
	if n%3==0:
		r+=r[-3:]
	else:
		r+=bin((n%3)*3)[2:]
	r=int(r,2)
	if r>76:
		print(n)
		exit()