for i in range(95632,95700+1):
    s=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            if j%2==0: s.append(j)
            if (i//j)!=j:
                if (i//j)%2==0: s.append(i//j)
    if len(s)==6:
        s.sort()
        print(i,s)