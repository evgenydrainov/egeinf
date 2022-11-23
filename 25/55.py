def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n=1
for i in range(5336748,5336835):
    if prime(i):
        print(n,i)
        n+=1