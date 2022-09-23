f = open("17-1.txt")
s = []
for i in f:
    s.append(int(i))
c = 0
mn = 1000000000
for i in range(len(s) - 1):
    if (s[i] % 7 == 0 and s[i + 1] % 17 != 0) or (s[i + 1] % 7 == 0 and s[i] % 17 != 0):
        c += 1
        mn = min(mn, s[i] + s[i + 1])
print(c, mn)