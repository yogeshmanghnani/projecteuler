#File made by Yogesh Manghnani

for c in range(1, 1001):
    for b in range(1, 1001):
        for a in range(1, 1001):
            if a<b and b<c:
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    print(a, b, c)
                    print(a*b*c)
            else:
                break
        