from collections import Counter

def get_checksum():
	
	two_count = 0
	three_count = 0

	has_two = lambda counts: (2 in counts.values()) == True
	has_three = lambda counts: (3 in counts.values()) == True

	with open("input.txt") as f:
		for line in f:
			line = line.strip()
			letter_counts = Counter(line)
			# print(sorted(letter_counts))
			# print(len(line))
			# print(len(letter_counts))
			if has_two(letter_counts):
				two_count += 1
			if has_three(letter_counts):
				three_count += 1

	return two_count * three_count


def get_common_letters():

	alpha = "abcdefghijklmnopqrstuvwxyz"

	first_keys = {}
	second_keys = {}

	with open("input.txt") as f:
		for line in f:
			line = line.strip()
			first_half = line[:14]
			second_half = line[14:]
			if first_half in first_keys:
				print("FOUND FIRST KEY")
			if second_half in second_keys:
				print("FOUND SECOND KEY")
			
			first_keys.setdefault(first_half, []).append(second_half)
			second_keys.setdefault(second_half, []).append(first_half)
	return (first_keys, second_keys)

result = get_common_letters()
print(result)

# How I actually solved the problem:

for key in result[0]:
	if result[0][key] > 2:
		print(key, result[0][key])

# and it was the first value to be printed.

# I was just perusing the output and happened
# to notice. :(      :)









result = get_common_letters()
print(result)

print(get_checksum())

