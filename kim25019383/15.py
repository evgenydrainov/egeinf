def D(n,m):
	return n%m==0
for A in range(1, 10**10):
	f=0
	for x in range(200):
		a = D(x,A) or (D(x,23) <= (not (50<=x<=70)))
		if a==0:
			f=1
			break
	if f==0:
		print(A)