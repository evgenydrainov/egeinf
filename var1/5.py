for i in range(256):
    s=bin(i)
    s=s[2:]
    while len(s)!=8: s="0"+s
    s=list(s)
    for j in range(len(s)):
        if s[j]=="0":
            s[j]="1"
        else:
            s[j]="0"
    s="".join(s)
    #print(i)
    #print(s)
    x=int(s,2)
    x-=i
    #print(x)
    #input()
    if x==111:
        print(i)
