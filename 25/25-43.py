n=1
for i in range(1547341, 1547409):
	prime=True
	for j in range(2, int(i**0.5)+1):
		if i%j==0:
			prime=False
			break
	if prime:
		print(n, i)
		n+=1