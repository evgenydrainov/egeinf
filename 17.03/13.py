G={
	"А":"ВБГ",
	"Б":"Е",
	"В":"ЗД",
	"Г":"Д",
	"Д":"ЗЖЕ",
	"Е":"ЖИ",
	"Ж":"И",
	"З":"И",
	"И":"КЛМ",
	"К":"НЛ",
	"Л":"Н",
	"М":"Н",
	"Н":"",
}
count=0
ANS=[]
def findPath(path,target):
	global count
	lastTown=path[-1]
	if lastTown==target and len(path)>1:
		count+=1
		print(path)
		ANS.append(path)
		return
	for town in G[lastTown]:
		if not town in path or town == target:
			findPath(path+town, target)
findPath("А","Н")
print(count)
print(ANS)
print(len(ANS))

c=0
for i in ANS:
	if "Е" in i:
		print(i)
		c+=1
print(c)


count=0
findPath("А","Е")
C=count

count=0
findPath("Е","Н")
print()
print()
print()
print(C,count)

