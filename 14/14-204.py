n=64**30+2**300-4
c=0
while n>0:
    if n%8==7:
        c+=1
    n//=8
print(c)