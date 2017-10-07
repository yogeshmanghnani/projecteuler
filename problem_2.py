def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)



sum_of_even=0

n=1
while(fibo(n)<4000000):
    if fibo(n)%2==0:
        sum_of_even+=fibo(n)
    n+=1
print(sum_of_even)