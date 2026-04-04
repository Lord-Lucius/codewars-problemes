def sort_by_binary_ones(numList):
	return sorted(numList, key=lambda x: (-bin(x).count('1'), x))


print(["{0:b}".format(bversion) for bversion in [1,15,5,7,3]])
print(sort_by_binary_ones([1,15,5,7,3]))