f=open("17.txt")
s=[]
for i in f:
    s.append(int(i))
mn=100000000000
for i in range(len(s)):
    if 100<=s[i]<=999 and s[i]%10==5:
        mn=min(mn,s[i])
count=0
mx=-10000000
for i in range(len(s)-1):
    if 100<=s[i]<=999 or 100<=s[i+1]<=999:
        if (s[i] + s[i+1]) % mn == 0:
            count+=1
            mx=max(mx, s[i] + s[i+1])
print(count, mx)