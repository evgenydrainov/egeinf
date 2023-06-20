f=open("24.txt")
s=f.readline()
count=1
mx=-1000000
for i in range(1, len(s)):
    count+=1
    if s[i] in "NOP" and s[i-1] in "NOP":
        count=1
    mx=max(mx, count)
print(mx)