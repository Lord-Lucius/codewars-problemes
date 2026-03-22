int min(int *array, int arrayLength) {
	int ret = 2147483647;

	for (int i = 0; i < arrayLength; i++)
		if (array[i] < ret)
			ret = array[i];
	return ret;
}

int max(int *array, int arrayLength) {
	int ret = -2147483648;

	for (int i = 0; i < arrayLength; i++)
		if (array[i] > ret)
			ret = array[i];
	return ret;
}