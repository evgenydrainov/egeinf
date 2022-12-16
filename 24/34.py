f=open("k7c-2.txt")
s=f.readline()
c=0
for i in range(len(s)-2):
    if (s[i] in "ACE") and (s[i+1] in "ADF") and (s[i+1]!=s[i]) and(s[i+2] in "ABF")and(s[i+2]!=s[i+1]):
        c+=1
print(c)