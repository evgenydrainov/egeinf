#100000000
# 3?458* 3
def base9(n):
    s=""
    while n>0:
        s=str(n%9)+s
        n//=9
    return s
for i in range(304583,40000000):
    s=str(i)
    if s[0]=="3" and s[2:5]=="458" and s[-1]=="3":
        j=base9(i)
        k="".join(sorted(j))
        k=k[::-1]
        if k==j:
            arr=list(j)
            arr=list(map(int,arr))
            print(i,sum(arr))
            
        
