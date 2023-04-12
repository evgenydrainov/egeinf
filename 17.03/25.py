N=860001
c=0
while True:
	M=0
	for i in range(2, int(N**0.5)+1):
		if N%i==0:
			M=(N/i)-i
			break
	if M%100==30:
		c+=1
		print(N,M)
		if c==5: break
	N+=1