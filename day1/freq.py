def calc_frequency():
	result = 0
	with open("input.txt") as f:
		for line in f:
			line = line.strip()

			if line[0] == "+":
				result += int(line[1:])
			elif line[0] == "-":
				result -= int(line[1:])

	return result

def find_repeat_frequency():
	frequencies = set([0])

	result = 0
	
	while True:
		with open("input.txt") as f:
			for line in f:
				line = line.strip()

				if line[0] == "+":
					result += int(line[1:])
				elif line[0] == "-":
					result -= int(line[1:])

				if result in frequencies:
					return result
				else: 
					frequencies.add(result)

print("part 1 result is", calc_frequency())

print("part 2 result is", find_repeat_frequency())