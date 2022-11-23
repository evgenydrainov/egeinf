n=8**20+((8**22-8**17)*(8**13+8**16))
n=oct(n)
n=n[2:]
n=n.replace("7","0")
n=n[0:len(n)-3]
s=0
for i in n:
    s += int(i)
print(s)