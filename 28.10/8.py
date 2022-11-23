i=0
n=0
alph="АВИКНСТ"
N=7
while True:
    s=""
    s+=alph[(n//N//N//N)%N]
    s+=alph[(n//N//N)%N]
    s+=alph[(n//N)%N]
    s+=alph[(n)%N]
    if s[0] in "ВКНСТ" and s[3] in "АИ":
        i+=1
        if s=="НИКА":
            print(i)
            break
    n+=1