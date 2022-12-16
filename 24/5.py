f=open("k7-25.txt")
s=f.readline()
c=0
mx=0
for i in s:
    if i=="C":
        c+=1
        mx=max(mx,c)
    else:
        c=0
print(mx)