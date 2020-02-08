def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

facts = [factorial(var) for var in range(0, 10)]

def get_digits(n):
	return [int(i) for i in str(n)]


def sum_of_fact(n):
	return sum([facts[i] for i in get_digits(n)])


upper_bound = 9
while(upper_bound<sum_of_fact(upper_bound)):
	upper_bound = (upper_bound*10)+9

nums = []
for i in range(10, upper_bound+1):
	if(sum_of_fact(i)==i):
		nums.append(i)

print(sum(nums))

