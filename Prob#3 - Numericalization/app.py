template = [
	[
		"00000",
		"0   0",
		"0   0",
		"0   0",
		"00000"
	],
	[
		"    1",
		"    1",
		"    1",
		"    1",
		"    1"
	],
	[
		"22222",
		"    2",
		"22222",
		"2    ",
		"22222"
	],
	[
		"33333",
		"    3",
		"33333",
		"    3",
		"33333"
	],
	[
		"4   4",
		"4   4",
		"44444",
		"    4",
		"    4"
	],
	[
		"55555",
		"5    ",
		"55555",
		"    5",
		"55555"
	],
	[
		"66666",
		"6    ",
		"66666",
		"6   6",
		"66666"
	],
	[
		"77777",
		"    7",
		"    7",
		"    7",
		"    7"
	],
	[
		"88888",
		"8   8",
		"88888",
		"8   8",
		"88888"
	],
	[
		"99999",
		"9   9",
		"99999",
		"    9",
		"99999"
	]
]

def isVisible(number, row, col):
	return template[number][row][col] != " "

pattern, m1, m2 = [e for e in input().strip().split()]
m1, m2 = [int(e) for e in [m1, m2]]

for row in range(5 * m1):
	for number in pattern:
		for col in range(5 * m2):
			number = int(number)
			print(number if isVisible(number, row//m1, col//m2) else " ", end="")
		print(" "*m2, end="")
	print()
