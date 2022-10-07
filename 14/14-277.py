ans=0
for i in range(2,11):
    n=611
    s=""
    while n>0:
        s=str(n%i)+s
        n//=i
    print(s,len(s))
    if len(s)%2==1:
        ans+=i
print("ans",ans)