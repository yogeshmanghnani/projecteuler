def get_digits(number):
	no_str = str(number)
	digits = []
	for i in no_str:
		digits.append(int(i))
	return digits

def get_sum_power(digits, power):
	if len(digits) <= 1:
		return 0
	to_ret = 0
	for i in digits:
		to_ret += i**power
	return to_ret

def find_numbers(power):
	numbers = []
	ubds = len(str(9**power * len(str(9**power))))
	upper_bound = int("9"*ubds)

	for i in range(upper_bound+1):
		if i == get_sum_power(get_digits(i), power):
			numbers.append(i)

	return numbers

print(sum(find_numbers(5)))
