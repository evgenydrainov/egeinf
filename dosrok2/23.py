def f(st,end):
	if st>end: return 0
	if st==end: return 1
	if st==11: return 0
	return f(st+1,end)+f(st*2,end)+f(st*3,end)
print(f(2,15)*f(15,25))