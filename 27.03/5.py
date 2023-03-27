#27432111
#74322111

n=27432111
while True:
	przv=1
	s=0
	for i in str(n):
		przv*=int(i)
		s+=int(i)
	if przv>s:
		r=str(przv)+str(s)
	else:
		r=str(s)+str(przv)
	if r=="33621":
		print(n)
	n+=1