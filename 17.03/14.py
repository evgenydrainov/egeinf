n=4**2022 - 2*(4**1111) + 16**600 + 192
print(n)
s=""
while n>0:
	s=str(n%4)+s
	n//=4
print(s)
print(s.count("3"))