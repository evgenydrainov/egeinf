mxs=0
mxi=0
for i in range(2,11):
    n=2345
    s=0
    while n>0:
        s+=n%i
        n//=i
    print(i,s)
    if s>mxs:
        mxs=s
        mxi=i
print("ans", mxi)