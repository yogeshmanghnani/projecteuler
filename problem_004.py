#File made by Yogesh Manghnani

largest = 1
k = 1
z = "init"
for i in range (100, 1000):
    for j in range (100, 1000):
        k=i*j
        z=str(k)
        if z == z[::-1] and k>largest:
            largest = k
            
            

print(largest)
