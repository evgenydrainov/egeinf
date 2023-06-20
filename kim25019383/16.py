#8262826164

#import sys
#sys.setrecursionlimit(10000)
#def f(n):
#	if n==1: return 1
#	if n>1: return n*f(n-1)
#print((f(2023) - f(2022)) / f(2020))

#f=[1]
#for n in range(2, 2023+1):
#	f.append(n * f[(n - 1) - 1])
#print((f[2022] - f[2021]) / f[2019])

pf=1
for n in range(2, 2023+1):
	f = n*pf
	pf = f
	if n==2022: f2022=f
	if n==2020: f2020=f
print((f - f2022) / f2020)