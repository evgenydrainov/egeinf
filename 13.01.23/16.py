def f(n):
    if n==0: return 0
    if n%2!=0: return (n-1)+1
    if n>0 and n%2==0: return f(n/2)
for i in range(0,1000000000):
    print(i,f(i),i/1000000000)