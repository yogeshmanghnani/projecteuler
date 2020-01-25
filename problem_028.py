answer = 0
for grid_width in range(1, int((1001+1)/2)+1):
	if grid_width == 1:
		answer += 1
		last = 1
	else:
		add = (grid_width - 1) * 2
		for i in range(4):
			last += add
			answer += last

print(answer)
