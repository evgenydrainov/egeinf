def f(st,end):
    if st>end: return 0
    if st==end: return 1
    if st==12: return 0
    return f(st+1,end) + f(st+2,end) + f(st*2,end)
print(f(2, 9) * f(9, 17))