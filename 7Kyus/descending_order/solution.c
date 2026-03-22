#include <inttypes.h>

uint64_t getLen(uint64_t n) {
	uint64_t len = 1;
	while ((n / 10) != 0) {
		len += 1;
		n = n / 10;
	}
	return (len);
}

void sortTab(uint64_t *t, uint64_t len) {
	uint64_t tmp = 0;

	for (uint64_t i = 1; i < len; i++) {
		if (t[i] > t[i - 1]) {
			tmp = t[i - 1];
			t[i - 1] = t[i];
			t[i] = tmp;
			i = 0;
		}
	}
}

uint64_t descendingOrder(uint64_t n) {
	uint64_t len = getLen(n);
	uint64_t t[len];
	uint64_t ret = 0;

	for (uint64_t i = 0; i < len; i++)
		t[i] = 0;
	for (uint64_t i = len - 1; n != 0; i--) {
		t[i] = n % 10;
		n = n / 10;
	}

	sortTab(t, len);
	for (uint64_t i = 0; i < len; i++)
		ret = ret * 10 + t[i];

	return (ret);
}