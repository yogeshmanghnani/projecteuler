def isprime(k):
    for i in range(2, int(k**0.5)+1):
        if k%i==0:
            return False
        else:
            return True
        
    

    
num = 600851475143
largestprime=0
j=2
while(num>1):
   if num%j==0 and isprime(j):
       num/=j
       largestprime=j
   j+=1
   
print(largestprime)