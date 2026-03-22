import math

def get_average(marks):
	return math.floor(sum(marks) / len(marks))

if __name__ == "__main__":
	print(get_average([2, 2, 2, 2, 2]))