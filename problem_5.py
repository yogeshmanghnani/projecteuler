found = False
j=0
n = 1
while(not found):
    j+=1
    factors = 1
    
    if j % 16 == 0:
        ## 2, 4, 8, 16
        factors += 4
    else:
        continue
    
    if j % 18 == 0:
        ## 3, 9, 6, 18
        factors += 4
    else:
        continue
    
    if j % 20 == 0:
        ## 5, 10, 20
        factors+=3
    else:
        continue
        
    if j % 14 == 0:
        ## 7, 14
        factors+=2
    else:
        continue
    
    if j%12==0:
        ## 12
        factors+=1
    else:
        continue
    
    
    if j%11==0:
        ## 11
        factors+=1
    else:
        continue
    
    if j%13==0:
        ## 13
        factors+=1
    else:
        continue
    
    
    
    if j%15==0:
        ## 15
        factors+=1
    else:
        continue
    
    
    if j%17==0:
        ## 17
        factors+=1
    else:
        continue
    
    
    if j%19==0:
        ## 19
        factors+=1
    else:
        continue
    
    
    
    
    
    
    
    
    
    if factors==20:
        break
    
    
    
        
        
        
print(j)
        
## 1
## 2, 4 , 8 , 16
## 3, 9, 6, 18
## 5, 10, 20
## 7, 14
## 12
## 11
## 13
## 15
## 17
## 19