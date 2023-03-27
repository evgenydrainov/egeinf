#799995 266662
#799990 399993
#799967 114274
#799956 399976
#799922 399959

c=0
for N in range(800000-1,0,-1):
	M=0
	for i in range(2,int(N**0.5)+1):
		if N%i==0:
			par=N//i
			if par!=i: M=par-i
			break
	if M!=0:
		if M%17==0:
			print(N,M)
			c+=1
			if c==5: exit()