#include <stdbool.h>

const char *bool_to_word(bool value) {
	if (value)
		return ("Yes");
	return ("No");
}