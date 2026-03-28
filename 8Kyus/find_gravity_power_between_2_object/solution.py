def resolve_conversion_kg(val, unit):
	new_val: float = 0
	match unit:
		case 'g':
			new_val = val / 1000
		case 'mg':
			new_val = val / 1000000
		case 'μg':
			new_val = val / 1_000_000_000
		case 'lb':
			new_val = val * 0.453592
	return new_val, "kg"

def resolve_conversion_m(val, unit):
	new_val: float = 0
	match unit:
		case 'cm':
			new_val = val / 100
		case 'mm':
			new_val = val / 1000
		case 'μm':
			new_val = val / 1_000_000
		case 'ft':
			new_val = val * 0.3048
	return new_val, "m"

def calcul_result(values: list):
	G = 6.67e-11
	result = G * (values[0] * values[1]) / (values[2] ** 2)
	return result

def solution(arr_val, arr_unit):
	# G = 6.67 x 10^-11 N . kg^-2 . m^2

	for i in range(len(arr_val)):
		if arr_unit[i] in ['g', 'mg', 'μg', 'lb']:
			arr_val[i], arr_unit[i] = resolve_conversion_kg(arr_val[i], arr_unit[i])
		elif arr_unit[i] in ['cm', 'mm', 'μm', 'ft']:
			arr_val[i], arr_unit[i] = resolve_conversion_m(arr_val[i], arr_unit[i])
	return calcul_result(arr_val)
