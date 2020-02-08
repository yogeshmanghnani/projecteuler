total = 0
for i in range(1, 1000000):
	if str(int(str(i)[::-1])) == str(i):
		if str(int(bin(i)[2:][::-1])) == bin(i)[2:]:
			total += i
print(total)
