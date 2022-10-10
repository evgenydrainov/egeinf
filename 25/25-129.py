for i in range(12034679, 23175822):
    nontriv=[]
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            nontriv.append(j)
            par = i//j
            if par!=j:
                nontriv.append(par)
            if len(nontriv)>3:
                break
    if len(nontriv)==3:
        print(i, nontriv[1])