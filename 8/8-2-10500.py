count = 0
for a in range(1, 5+1):
    for b in range(1, 5+1):
        for c in range(1, 5+1):
            for d in range(1, 5+1):
                for e in range(1, 5+1):
                    ones = 0
                    if a==1:
                        ones += 1
                    if b==1:
                        ones += 1
                    if c==1:
                        ones += 1
                    if d==1:
                        ones += 1
                    if e==1:
                        ones += 1
                    
                    if ones == 3:
                        count += 1
print(count)