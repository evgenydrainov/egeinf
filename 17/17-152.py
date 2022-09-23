f = open("17-1.txt")
s = []
for i in f:
    s.append(int(i))
c = 0
mx = -100000000
for i in range(len(s) - 1):
    if (s[i] % 9 == 0 and s[i + 1] % 8 == 3 and s[i + 1] % 9 != 0) or (s[i + 1] % 9 == 0 and s[i] % 8 == 3 and s[i] % 9 != 0):
        mx = max(mx, s[i], s[i + 1])
        c += 1
print(c, mx)