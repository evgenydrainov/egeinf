for i in range(2, 30001):
#for i in [220]:
    si=[]
    for x in range(1, int(i**0.5)+1):
        if i%x == 0:
            si.append(x)
            par = i // x
            if par != x:
                if par != i:
                    si.append(par)
    
    #for j in range(i+1, 30001):
    #for j in [284]:
    for j in [sum(si)]:
        #if j!=sum(si):
        #    continue
        
        if j<=i:
            continue

        sj=[]
        for y in range(1, int(j**0.5)+1):
            if j%y == 0:
                sj.append(y)
                par = j // y
                if par != y:
                    if par != j:
                        sj.append(par)
        
        if sum(si)==j and sum(sj)==i:
            print(i, j)