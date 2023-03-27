f=open("zadanie24_1.txt")
s=f.readline()
c=1
mx=-100000
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        c+=1
        mx=max(mx,c)
    else:
        c=1
print(mx)