# ZZ8???54???22ZZ
# 012345678901234
# 15
f=open("24.txt")
s=f.readline()
a="0123456789"
mx=-100000000000
for i in range(0,len(s)-14):
	if s[i]=="Z" and s[i+1]=="Z" and s[i+13]=="Z" and s[i+14]=="Z":
		if s[i+2]=="8" and s[i+6]=="5" and s[i+7]=="4" and s[i+11]=="2" and s[i+12]=="2":
			if (s[i+3] in a) and (s[i+4] in a) and (s[i+5] in a) and (s[i+8] in a) and (s[i+9] in a) and (s[i+10] in a):
				n=int(s[i+2:i+2+11])
				mx=max(mx,n)
print(mx)
b=1
for i in str(mx):
	if int(i)%2!=0:
		b*=int(i)
print(b)