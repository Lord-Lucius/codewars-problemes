def _all(seq, fun):
	for elem in seq:
		if not fun(elem):
			return False
	return True