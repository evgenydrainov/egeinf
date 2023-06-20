count=0
for n in range(1000, 9999+1):
	r=list(str(n))
	if int(r[0])%4==0: r[0]="9"
	elif int(r[0])%2==0: r[0]="3"
	
	r=int("".join(r))
	
	#print(n, r)
	#input()
	
	if str(r)[0]=="9" and oct(r)[-1]=="4": count+=1
print(count)