A=0
while True:
    fl=0
    for x in range(300):
        f = (((x & 52) != 0) and ((x & 36) == 0)) <= ((x & A) != 0)
        if f==0:
            fl=1
            break
    if fl==0:
        print(A)
        break

    A+=1