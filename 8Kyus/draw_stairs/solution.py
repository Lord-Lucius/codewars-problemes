def draw_stairs(n):
	append_string = ""
	for i in range(0, n):
		append_string += (" "*i) + "I" + ("\n" if i + 1 != n else "")
	return append_string
