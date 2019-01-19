#conding=utf-8
lis = [1,2,3,4,5]
def get_median(data):
	data.sort()
	half = len(data) // 2
	return (data[half] + data[~half]) / 2
res = get_median(lis)
print(res)