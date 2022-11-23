s="АКЛОШ"
count=0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    sl=a+b+c+d+e
                    if ("А" in sl) or ("О" in sl):
                        count += 1
print(count)
