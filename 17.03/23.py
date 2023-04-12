def f(st,end):
	if st==end: return 1
	if st>end: return 0
	return f(st+2,end) + f(st+7,end)
print(f(7,51))