cnt=0
for a in "12345":
    for b in "12345":
        for c in "12345":
            for d in "12345":
                for e in "12345":
                    s=a+b+c+d+e
                    if s.count("1")==3:
                        cnt+=1
print(cnt)
