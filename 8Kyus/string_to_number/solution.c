int string_to_number(const char *src) {
	int ret = 0;
	int i = 0;
	int sign = 1;

	if (src[i] == '-' || src[i] == '+') {
		i++;
		sign = -sign;
	}
	for (; i < strlen(src); i++) {
		ret = (ret * 10) + (src[i] - '0');
	}
	ret = ret * sign;
	return ret;
}