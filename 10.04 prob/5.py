n=1
mx=-10000000000
while True:
	r=bin(n)[2:]
	while len(r)<3: r="0"+r
	#print(r)
	#print(r[-3:])
	#input()
	if n%3==0:
		r+=r[-3:]
	else:
		r+=bin(3*(n%3))[2:]
	i=int(r,2)
	print("n", n, "r", r, i)
	#input()
	
	#if i > 100:
	#	break
	if n > 30:
		break
	if i<100:
		mx=max(mx,n)
	n+=1
print(mx)