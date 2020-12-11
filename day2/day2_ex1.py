import os

with open("day2_input.txt") as f:
	data = f.readlines()

data = [x.strip() for x in data]

content = [x.split(' ') for x in data]

def is_pw_valid(pw_list):
	'''
	psuedocode:
	instantiate valid_pw count
	for each input:
		get min and max from 1st string
		get letter from 2nd string
		get pw string
		check letter count
		if letter count >= min and letter count <= max
			valid_pw_count += 1
		else:
			pass
	return valid_pw_count
	'''
	valid_count = 0
	for pw in pw_list:
		min_max = pw[0].split('-')
		min_ct = int(min_max[0])
		max_ct = int(min_max[1])
		# print(min_ct, max_ct)

		letter_to_test = pw[1].replace(':', '')
		# print(letter_to_test)

		# print(pw[2])

		letter_count = pw[2].count(letter_to_test)
		# print(letter_count)

		if min_ct <= letter_count <= max_ct:
			# print(True)
			valid_count += 1
		else:
			# print(False)
			pass
	print(valid_count)


is_pw_valid(content)

