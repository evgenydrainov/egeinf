G={
	"А":"ВБГ",
	"Б":"ДЕ",
	"В":"ЗД",
	"Г":"ЕИ",
	"Д":"ЗЖЕ",
	"Е":"ЖИ",
	"Ж":"И",
	"З":"И",
	"И":"КЛМ",
	"К":"ЛН",
	"Л":"Н",
	"М":"ЛН",
	"Н":"",
}
count = 0
def findPath(path, target):
	global count
	lastTown = path[-1]
	if lastTown == target and len(path) > 1:
		if "Е" in path:
			count += 1
			print(path)
		return
	for town in G[lastTown]:
		if not town in path or town == target:
			findPath(path + town, target)
findPath("А", "Н")
print(count)