for i in range(102714,102726):
    s=[]
    for j in range(1,i+1):
        if i%j==0:
            s.append(j)
    if len(s)==4:
        print(s)