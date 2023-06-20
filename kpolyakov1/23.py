all=[]

def f(st,end,a):
	if st==end:
		e=a.copy()
		e.append(st)
		all.append(e)
		return 1
	if st>end: return 0
	
	b=a.copy()
	b.append(st)
	
	c=a.copy()
	c.append(st)
	
	d=a.copy()
	d.append(st)
	
	return f(st+2,end,b)+f(st*3,end,c)+f(st*4,end,d)

print(f(1,600,[]))

print(len(all))

print(all[0])

c=0
for i in all:
	for j in range(0,len(i)-2):
		if (i[j]+i[j+1]+i[j+2])%11==0:
			c+=1
			break

print(c)