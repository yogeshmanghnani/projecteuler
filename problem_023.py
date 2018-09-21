def findAllPerfectDivisors(number):
    divisors = [1]
    for i in range(2,int((number**0.5))+1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(int(number/i))
    return list(set(divisors))
    

def isAbundant(n):
    if n<1:
        return False
    divisors = findAllPerfectDivisors(n)
    return sum(divisors, 0) > n


def isSumOfTwoAbudantNumbers(n):
    upperBoundOfLoop = int(n/2) + 1
    for i in range(1, upperBoundOfLoop):
        if isAbundant(i) and isAbundant(n-i):
            return True
    return False


lista = []
for i in range(1, 28124):
    if not isSumOfTwoAbudantNumbers(i):
        lista.append(i)


print(sum(lista, 0))
