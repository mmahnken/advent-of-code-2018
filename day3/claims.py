def create_claims():
	"""
		{
		 X: {Y:[claim num, claim num], 1, 2, 3},
		 1: {0, 1, 2, 3}, 

		 # ...
		}
	"""

	claims = {}
	claims_info = {}

	with open("input.txt") as f:
		for line in f:
			claim_num, size_info = line.split(' @ ')

			coords, dimensions = size_info.split(': ')
			x, y = [int(x) for x in coords.split(',')]
			width, height = [int(x) for x in dimensions.split('x')]

			claims_info[claim_num] = width*height
			
			temp_y = y
			non_overlapping = True
			for inch in range(height):
				temp_x = x
				for inch2 in range(width):
					claims.setdefault(temp_x, {}).setdefault(temp_y, []).append(claim_num)
					temp_x = temp_x + 1
				temp_y = temp_y + 1
	return (claims, claims_info)

def find_overlapping(claims):
	"""To solve part 1"""

	two_or_more = 0
	for x in claims:
		for y in claims[x]:
			if len(claims[x][y]) > 1:
				two_or_more += 1

	return two_or_more

def find_non_overlapping(claims, claims_info):
	"""To solve part 2"""

	nonoverlaps = {}

	for x in claims:
		for y in claims[x]:
			if len(claims[x][y]) == 1:
				claim_num = claims[x][y][0]
				new_value = nonoverlaps.get(claim_num, 0) + 1
				nonoverlaps[claim_num] = new_value
	print(nonoverlaps)

	for claim in nonoverlaps:
		if nonoverlaps[claim] == claims_info[claim]:
			return claim

c, c_info = create_claims()
# print(find_overlapping(c))
# print(find_non_overlapping(c, c_info))