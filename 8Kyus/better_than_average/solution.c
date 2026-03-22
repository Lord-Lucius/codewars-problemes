#include <stdbool.h>

bool better_than_average(const int class_points[], int class_size, int your_points) {
	// Your code here :)
	// Note: `class_size` is the length of `class_points`.
	int res = 0;
	int i = 0;
	for (; i < class_size; i++) {
		res += class_points[i];
	}
	res /= i;
	if (your_points > res)
		return (true);
	return false;
}