n = 214
s = ""
while n > 0:
    s = str(n % 4) + s
    n //= 4
print(s)