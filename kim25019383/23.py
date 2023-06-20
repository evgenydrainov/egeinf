def f(st, end):
	if st > end: return 0
	if st == end: return 1
	return f(st+3, end) + f(st+1, end) + f(st*3, end)
print(f(1, 34))