def sum_digits(n):
	s = 0
	while n > 0:
		s += n % 10
		n //= 10
	return s

c = 0
mn = 100000000
for i in range(3721, 7752 + 1):
	if (sum_digits(i) % 3) == 0 and (i % 8 != 0):
		c += 1
		mn = min(mn, i)
print(c, mn)