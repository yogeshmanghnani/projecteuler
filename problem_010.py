#File made by Yogesh Manghnani

def checkIfPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    w = 2
    i = 5
    while(i<= (n**0.5 + 1)):
        if n%i == 0 :
            print(i)
            return False
        
        i += w
        w += 6-w
    
    return True


if __name__ == "__main__":
    upperBound = 600
    accu = 0
    for i in range(upperBound+1):
        if checkIfPrime(529):
            accu += i
    
    print(accu)
        
    