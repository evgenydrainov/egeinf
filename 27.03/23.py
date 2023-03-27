def f(st,end):
	if st>end: return 0
	if st==end: return 1
	return f(st+2,end)+f(st+10,end)
print(f(5,71))