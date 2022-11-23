for i in range(1, 256):
    b=i-1
    #print(bin(b))
    for j in range(0, 8):
        b ^= (1 << j)
    #print(bin(b))
    #input()
    if b==178:
        print(i)