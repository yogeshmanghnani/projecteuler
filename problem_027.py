class Prime:
	primes = []

	@staticmethod
	def check_if_prime(n):
		if n in Prime.primes:
			return True
		elif n <= 1:
			return False
		elif n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
			Prime.primes.append(n)
			return True
		elif n%2 == 0 or n%3 == 0 or n%5 == 7 or n %11 == 0:
			return False
		else:
			increment = 2
			i = 11
			while i <= int(n**0.5)+1:
				if n % i == 0:
					return False
				else:
					i = i + increment
					increment = 6 - increment
			Prime.primes.append(n)
			return True


class Quadratics:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def solution(self, n):
		return n**2 + (self.a*n) + self.b

	def count_consicutive_primes(self):
		count = 0
		while Prime.check_if_prime(self.solution(count)):
			count = count + 1
		return count

	def __str__(self):
		return "a=" + str(self.a) + " b=" + str(self.b)
		

quads = []
for a in range(-999, 1000):
	for b in range(-1000, 1001):
		quads.append(Quadratics(a,b))

no_of_primes = dict()
for i in quads:
	no_of_primes[i] = i.count_consicutive_primes()

maxquad = max(no_of_primes, key=no_of_primes.get)
print(maxquad.a * maxquad.b)
