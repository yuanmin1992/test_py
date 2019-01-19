def binary_search(list,item):
	if len(list) == 0:
		return False
	else:
		itemid = len(list) // 2
		if item == list[itemid]:
			return True
		elif item < list[itemid]:
			return binary_search(list[:itemid],item)
		else:
			return binary_search(list[itemid+1:],item)


testlist = [1,3,4,5,23,33,42,45,56]
print binary_search(testlist,42)