def count_recurring_digits(nu, de):
	num = nu
	rems = []
	while True:
		rem = num % de
		if rem in rems:
			return len(rems)
		elif rem == 0:
			return 0
		else:
			rems.append(rem)
		num = rem * 10


dict_of_num_of_recurring_digits = dict()

for i in range(1, 1000):
	dict_of_num_of_recurring_digits[i] = count_recurring_digits(1, i)

answer = max(dict_of_num_of_recurring_digits, key=dict_of_num_of_recurring_digits.get)
print(answer)
