for i in range(2,263001):
	s=0
	for j in range(1,int(i**0.5)+1):
		if i%j==0:
			s+=j
			if j!=i//j:
				s+=i//j
	s1=0
	for k in range(1,int(s**0.5)+1):
		if s%k==0:
			s1+=k
			if k!=s//k:
				s1+=s//k
	if s1==i*2:
		print(i)