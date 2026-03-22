#include <stddef.h>

long long sum_two_smallest_numbers(size_t n, const int numbers[n]) {
	long long low1 = 12031231203123;
	long long low2 = 12031231203123;
	int index = 0;
	for (size_t i = 0; i < n; i++) {
		if (numbers[i] < low1) {
			low1 = numbers[i];
			index = i;
		}
	}
	for (size_t i = 0; i < n; i++) {
		if (numbers[i] < low2 && i != index)
			low2 = numbers[i];
	}
	return low1 + low2;
}