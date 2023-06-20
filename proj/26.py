f=open("26.txt")
K=int(f.readline())
N=int(f.readline())
s=[]
j=0
for i in f:
    a=i.split()
    st=int(a[0])
    end=int(a[1])
    s.append([st, 0, end])
    j+=1
s.sort()
cell=[-1]*K
count=0
for i in s:
    for j in range(K):
        if i[0] > cell[j]:
            cell[j] = i[2]
            count+=1
            q=j+1
            break
print(count, q)