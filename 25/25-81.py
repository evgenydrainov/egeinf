for i in range(2, 263001):
    s=[]
    for j in range(1, int(i**0.5)+1):
        if i%j == 0:
            s.append(j)
            par = i // j
            if par != j:
                s.append(par)
    ssum=sum(s)
    s=[]
    for j in range(1, int(ssum**0.5)+1):
        if ssum%j == 0:
            s.append(j)
            par = ssum // j
            if par != j:
                s.append(par)
    if sum(s)==i*2:
        print(i)