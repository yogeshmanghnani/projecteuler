class Prime:
	primes = []

	@staticmethod
	def check_if_prime(n):
		if Prime.primes[n]:
			return True
		else:
			return False
	
	@staticmethod
	def get_primes_below_n(n=1000001):
		"""
		Seive of Eratosthenes
		"""
		from math import ceil
		round_up = lambda n, prime: int(ceil(float(n)/prime))

		primes = [True]*n
		primes[0] = False
		primes[1] = False
		prime_list = []

		for current_prime in range(2, n):
			if not primes[current_prime]:
				continue
			prime_list.append(current_prime)
			for multiplicant in range(2, round_up(n, current_prime)):
				primes[current_prime * multiplicant] = False
		Prime.primes = primes
		return prime_list



def rotate(num):
	lista = []
	for i in range(len(str(num))):
		lista.append(int(str(num)[i:] + str(num)[:i]))
	return lista


primes_till_mil = Prime.get_primes_below_n()


print("Starting to count")
count = 0
for i in primes_till_mil:
	rota = rotate(i)
	if len(rota) == len(list(filter(Prime.check_if_prime, rota))):
		print("Found", i)
		count += 1

print(count)
