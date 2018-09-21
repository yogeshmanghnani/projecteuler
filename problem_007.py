#File made by Yogesh Manghnani

# The below function is the AKS primality test.
def check_if_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 5:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    k = 5
    np = 2
    omega = 4

    while k < (n ** 0.5) + 1:
        if n % k == 0:
            return False
        else:
            k += np
            np = omega
            omega = 6 - omega

    return True


if __name__ == '__main__':
    i = 1
    j = 0
    dic_of_prime = {}
    while j <= 10001:
        if check_if_prime(i):
            j += 1
            dic_of_prime[j] = i
        i += 1

    print(dic_of_prime[10001])
