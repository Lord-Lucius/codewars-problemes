def is_isogram(string):
	string = string.lower()
	if not string:
		return True
	for char in string:
		if string.count(char) > 1:
			return False
	return True

if __name__ == "__main__":
	print(is_isogram("Dermatoglyphics"))