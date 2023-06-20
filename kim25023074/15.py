def D(n,m): return n%m==0
A=1
count=0
while True:
	fl=0
	for x in range(200):
		f = D(x, A) or ((70 <= x <= 80) <= (not D(x, 18)))
		if f==0:
			fl=1
			break
	if fl==0:
		count += 1
		print(A, count)
	A+=1