def find_slope(points):
	numerator = points[3] - points[1]
	denominator = points[2] - points[0]
	if denominator != 0:
		return str(numerator // denominator)
	return "undefined"