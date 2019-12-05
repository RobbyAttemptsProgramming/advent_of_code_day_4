"""
Robert Hamby
December 5, 2019
Advent of Code Day 4 Part 1
https://adventofcode.com/2019/day/4/answer
"""

# Takes in a number, converts to a string and
# compares each index's value. If the current
# number is ever greater than the next, it returns
# false. Otherwise, returns true
def decrease_test(s):
	num = str(s)
	length = len(num) - 1

	for i in range(0, length):
		if num[i] > num[i + 1]:
			return False

	return True

# Tests if a number and adjacent number are the same but 
# does not repeat more than twice adjacently
# e.g. : 223456 returns true because 2 repeats but no more than twice in a row
#		 222345 returns false because 2 repeats more than twice in a row
def adjacent_test(s):
	num = str(s)
	length = len(num)

	for i in range(0, length):
		if i + 1 >= length:
			break
		else:
			if num[i] == num[i + 1] and num.count(num[i]) == 2:
				return True

# Performs adjacent_test, decrease_test, and a length
# check to verify whether the argument number is a 
# possible password
def check_password(s):
	pass_len = 6
	
	if len(str(s)) != pass_len:
		return False

	if not decrease_test(s):
		return False

	if not adjacent_test(s):
		return False

	return True

# Cycles through the minimum and maximum numbers
# and checks whether each is a password. A counter
# keeps track of potential passwords
def count_passwords(minimum, maximum):
	count = 0

	for i in range(minimum, maximum + 1):
		if check_password(i):
			count += 1
			print("{} is true".format(i))

	return count

# Convert puzzle_input into a list to then
# convert into a min and max number to search
puzzle_input = "246540-787419"
puzzle_input = puzzle_input.split('-')
puzzle_range = []
for n in puzzle_input:
	puzzle_range.append(int(n))	

puzzle_min = puzzle_range[0]
puzzle_max = puzzle_range[1]

print(count_passwords(puzzle_min, puzzle_max))

