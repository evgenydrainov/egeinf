f=[7, 7]
for n in range(2, 12950+1):
	f.append(7 * f[n-2])
print(f[12950] / (7**6473))