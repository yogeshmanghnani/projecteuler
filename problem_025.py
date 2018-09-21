#File created by Yogesh Manghnani

fibonacci = {1:1, 2:1}

def fibon(n):
    if n not in fibonacci:
        fibonacci[n] = fibon(n-1) + fibon(n-2)
    
    
    return fibonacci[n]

n=1
flag = True
while flag:
    if len(str(fibon(n))) == 1000:
        print(n)
        flag = False
    n = n + 1
