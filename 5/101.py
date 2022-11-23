for x in range(10,100000):
	y=str(x%4)
	y+=str(x%2)
	y+=str(x%3)
	if y=="112":
		print(x)
		break