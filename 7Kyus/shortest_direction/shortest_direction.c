#include <stdio.h>

int normalise(long long n) {
	// always normalise
	n = n % 360;

	if (n > 180)
		n -= 360;
	else if (n <= -180)
		n += 360;
	return (n);
}

int shortest_direction(long long a, long long b) {
	a = normalise(a);
	b = normalise(b);

	int diff = b - a;

	if (diff > 180)
		diff = diff - 360;
	else if (diff < -180)
		diff = diff + 360;
	return (diff);
}