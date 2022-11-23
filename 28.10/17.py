f=open("17-199.txt")
s=[]
for i in f:
    s.append(int(i))
c=0
mx=-1000000
for i in range(0, len(s)-2):
    if s[i+1]>0 and (100<=s[i+1]<=999) and s[i+1]%2==1:
        c+=1
        mx=max(mx,s[i]+s[i+1]+s[i+2])
print(c)
print(mx)