/*    N.B. do not allocate memory,
   instead: return a string literal  */
#include <math.h>

const char *bmi(int weight, double height) {
	float bmi = weight / (height * height);
	if (bmi <= 18.5)
		return "Underweight";
	else if (bmi <= 25.0)
		return "Normal";
	else if (bmi <= 30.0)
		return "Overweight";
	return "Obese";
}