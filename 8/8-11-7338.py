alph = "katep"
count = 0
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        if a == "p" and f == "k":
                            count += 1
print(count)