#  0 1 2 3 4
h=[1,1,1,1,1]
for n in range(5,2009):
	if n%2!=0:
		h.append(1)
	else:
		h.append(h[n-1] + h[n-2] + h[n-3])
print(h[2008]-h[2006])