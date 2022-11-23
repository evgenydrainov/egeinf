for i in range(177399,177454):
    s=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            s.append(j)
            par=i//j
            if par!=j:
                s.append(par)
        if len(s)>6:
            break
    if len(s)==6:
        s.sort()
        print(s)