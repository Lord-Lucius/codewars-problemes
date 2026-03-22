void neutralize(const char *s1, const char *s2, char *s3) {
	// write to s3
	*s3 = '\0';
	for (int i = 0; s1[i]; i++) {
		while (*s3++)
			;
		if (s1[i] == s2[i])
			*(s3 - 1) = s1[i];
		else
			*(s3 - 1) = '0';
		*s3 = '\0';
	}
}