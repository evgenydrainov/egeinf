f=open("27_A.txt")
K=int(f.readline())
N=int(f.readline())
s=[]
for i in f:
    s.append(int(i))
mx=-1000000000
for i in range(N-1):
    for j in range(i+1, N):
        if j-i>=K:
            mx=max(mx, s[i]+s[j])
print(mx)