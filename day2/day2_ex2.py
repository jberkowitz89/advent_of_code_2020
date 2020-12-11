import os

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
		get first positionm and second position from 1st string
		get letter from 2nd string
		get pw_string
		check letter count
		if pw_string first position != letter and pw_string second position != letter
			pass
		elif pw_string first position == letter and pw_string second position == letter
			pass
		else
			valid_pw_count += 1

	return valid_pw_count
	'''
	valid_count = 0
	for pw in pw_list:
		p1_p2 = pw[0].split('-')
		pos_1 = int(p1_p2[0]) - 1
		pos_2 = int(p1_p2[1]) - 1

		letter_to_test = pw[1].replace(':', '')

		str_to_test = pw[2]
		
		if str_to_test[pos_1] != letter_to_test and str_to_test[pos_2] != letter_to_test:
			pass
		elif str_to_test[pos_1] == letter_to_test and str_to_test[pos_2] == letter_to_test:
			pass
		else:
			valid_count += 1

	print(valid_count)

is_pw_valid(content)

