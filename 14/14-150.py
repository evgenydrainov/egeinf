n = 2 * (9**10) - 3**5 + 5
c = 0
while n > 0:
    if n % 3 == 2:
        c += 1
    n //= 3
print(c)