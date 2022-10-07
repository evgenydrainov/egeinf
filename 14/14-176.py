n = 9 ** 17 + 3 ** 16 - 27
a = [0,0,0]
while n > 0:
    a[n%3] += 1
    n //= 3
print(max(a))