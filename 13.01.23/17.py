f=open("17.txt")
s=[]
for i in f:
    s.append(int(i))
c=0
mx=-10000000
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if (s[i]+s[j])%8==0:
            c+=1
            mx=max(s[i]+s[j],mx)
print(c,mx)