mn = 1000000000000
mx = -100000000000
for i in range(1000, 9999 + 1):
	if (i % 5 != 0) and (i % 7 != 0) and (i % 11 != 0):
		if (3 ** 7) <= i < (3 ** 8):
			mn = min(mn, i)
			mx = max(mx, i)
print(mn, mx)