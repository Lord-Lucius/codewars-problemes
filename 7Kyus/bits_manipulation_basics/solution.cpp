int toggle_bit(int n, unsigned pos) {
	int ret = n ^ (1 << pos);
	return ret;
}

int set_bit(int n, unsigned pos) {
	int ret = n | (1 << pos);
	return ret;
}

int clear_bit(int n, unsigned pos) {
	int ret = n & ~(1 << pos);
	return ret;
}

bool is_bit_set(int n, unsigned pos) { return (n & (1 << pos)) ? true : false; }

int set_multiple_bits(int n, unsigned mask) {
	int ret = n | mask;
	return ret;
}

int clear_multiple_bits(int n, unsigned mask) {
	int ret = n & ~mask;
	return ret;
}

int toggle_multiple_bits(int n, unsigned mask) {
	int ret = n ^ mask;
	return ret;
}