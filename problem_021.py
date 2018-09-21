#File created by Yogesh Manghnani

def get_divisors_of(number):
    to_return = []
    for i in range(1, int(number**0.5)):
        if number % i == 0:
            to_return.append(i)
            to_return.append(number//i)
            to_return.sort()
    return to_return


def d(n):
    divisors = get_divisors_of(n)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors >= n:
        sum_of_divisors -= n
    return sum_of_divisors


def check_if_amicable(number):
    second_number = d(number)
    temp = d(second_number)
    return temp == number and second_number != number


if __name__ == "__main__":
    print(check_if_amicable(220))
    sum_of_amicable = 0
    for i in range(1, 10001):
        if check_if_amicable(i):
            print(i)
            sum_of_amicable += i
    print(sum_of_amicable)
