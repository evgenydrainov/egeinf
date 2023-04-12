def f(n):
	if n<=1: return 1
	if n>1 and n%2!=0: return 4*n + f(n-1) - f(2)
	if n>1 and n%2==0: return 3*f(n-1)
print(f(35))
