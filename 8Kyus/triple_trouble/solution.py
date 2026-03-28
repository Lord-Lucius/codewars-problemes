def triple_trouble(one, two, three):
	n_string = ""

	for i in range(len(one)):
		n_string += one[i] + two[i] + three[i]
	return n_string

print(triple_trouble("aaa", "bbb", "ccc"))
