f=open("17.txt")
s=[]
for i in f:
	s.append(int(i))

def trehzn(x):
	return 100<=x and x<=999

mn=1000000000000000
for i in s:
	if trehzn(i) and (i%10==5):
		mn=min(mn,i)

print(mn)

c=0
mn_=10000000000000
for i in range(len(s)-1):
	if (trehzn(s[i]) and not trehzn(s[i+1])) or (trehzn(s[i+1]) and not trehzn(s[i])):
		if (s[i]+s[i+1])%mn==0:
			c+=1
			mn_=min(mn_,s[i]+s[i+1])

print(c)
print(mn_)