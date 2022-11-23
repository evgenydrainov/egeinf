for i in range(190061,190081):
    s=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            if j%2!=0:
                s.append(j)
            par=i//j
            if par!=j:
                if par%2!=0:
                    s.append(par)
            if len(s)>4:
                break
    if len(s)==4:
        s.sort(reverse=True)
        print(s)