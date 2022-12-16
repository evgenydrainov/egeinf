for i in range(4234679,10157813):
	if int(i**0.5)**2==i:
		c=0
		mx=-1000000000
		for j in range(2,int(i**0.5)+1):
			if i%j==0:
				c+=1
				mx=max(mx,j)
				if j!=i//j:
					c+=1
					mx=max(mx,i//j)
		if c==3:
			print(i,mx)