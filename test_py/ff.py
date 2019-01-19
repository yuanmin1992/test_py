def fun(n):
	list1 = []
	for i in range(n):
		if i == 0 or i == 1:
			list1.append(1)
			
		else:
			list1.append(list1[i-1]+list1[i-2])
	print list1


fun(8)