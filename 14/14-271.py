n=17**5+85**8-10
c=0
while n>0:
    if n%17==16:
        c+=1
    n//=17
print(c)