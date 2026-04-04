def max_rot(n):
	s = str(n)
	max_val = n
	for i in range(len(s)):
		s = s[:i] + s[i+1:] + s[i]
		max_val = max(max_val, int(s))

	return (max_val)