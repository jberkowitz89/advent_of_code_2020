
with open('day1_ex1_input.txt') as f:
	input = f.readlines()

input = [x.strip() for x in input]
input = [int(x) for x in input]

#checking if list contains unique elements
# print(len(input))
# print(len(set(input)))

for ix, i in enumerate(input):
	for nx, n in enumerate(input):
		if i == n:
			pass
		elif i + n == 2020:
			print(i, n)
			print(i * n)
		else:
			pass