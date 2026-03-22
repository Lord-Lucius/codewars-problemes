#include <stdbool.h>

bool was_package_received_yesterday(int tz_from, int tz_to, int start, int duration) {
	if ((start - (tz_from - tz_to) + duration) < 0) {
		return (true);
	}
	return false;
}