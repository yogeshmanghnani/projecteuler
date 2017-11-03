fact_dict={}
fact_dict[1]=1

def fact(n):
    if n in fact_dict.keys():
        return fact_dict[n]
    else:
        fact_dict[n] = n * fact(n-1)
        return fact_dict[n]
    

fact_of_100 = str(fact(100))


sum_of_digits = 0


for digit in fact_of_100:
    sum_of_digits += int(digit)


print(sum_of_digits)