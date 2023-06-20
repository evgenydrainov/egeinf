f=open("17.txt")
s=[]
for i in f:
	s.append(int(i))
def D(x):
	return 10<=x and x<=99
mx=-100000000
for i in range(len(s)):
	if D(s[i]):
		mx=max(mx,s[i])
c=0
MX=-10000000
for i in range(len(s)-1):
	if not( (D(s[i]) and not D(s[i+1])) or (D(s[i+1]) and not D(s[i])) ):
		continue
	if (s[i]+s[i+1]) % mx == 0:
		c+=1
		MX=max(MX,s[i]+s[i+1])
print(c,MX)