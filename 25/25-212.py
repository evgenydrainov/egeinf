for a in "FEDCBA9876543210":
    for b in "FEDCBA9876543210":
        s="1"+a+"DED"+b+"BABA"
        s=int(s,16)
        if s%186==0:
            print(s,s//186)
