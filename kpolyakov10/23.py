def f(st,end,k1,k2,k3):
	if st>end: return 0
	if st==end:
		if k2>=2 and k3==5: return 1
		return 0
	if k1>4: return 0

	return f(st*5,end,k1+1,k2,k3)+f(st*3,end,k1,k2+1,k3)+f(st+45,end,k1,k2,k3+1)
print(f(1,2970,0,0,0))