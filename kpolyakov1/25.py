# 17_000_000
# *1?*?68*
#  01 345
# %161==0
# 10068
# 01234
# 10143

c=0
for a in range(10143, 17_000_001, 161):
	s=str(a)
	if ("10" in s or "11" in s or "12" in s or "13" in s or "14" in s or "15" in s or "16" in s or "17" in s or "18" in s or "19" in s) and\
		("068" in s or "168" in s or "268" in s or "368" in s or "468" in s or "568" in s or "668" in s or "768" in s or "868" in s or "968" in s):
		i=s.index("1")
		i+=1
		j=s.rindex("68")
		j-=1
		if (j-i)>=1:
			if (c%500)==0:
				print(a, a/161)
			c+=1
			#print(i,j)

print()
print()

c=0

import re
p=re.compile("1\d\d+68")
p2=re.compile("\d+1\d\d+68")

for a in range(10143, 17_000_001, 161):
	s=str(a)
	if p.match(s) or p2.match(s):
		if (c%500)==0:
			print(a, a/161)
		#print(a, a/161)
		c+=1
print(c)