for i in range(1820348,2880928):
    s=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            s.append(j)
            par=i//j
            if par!=j:
                s.append(par)
            if len(s)>5:
                break
    if len(s)==5:
        s.sort()
        print(s)