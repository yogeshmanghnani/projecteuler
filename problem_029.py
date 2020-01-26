nos = set()
for a in range(2, 101):
	for b in range(2, 101):
		nos.add(a**b)

print(len(nos))
