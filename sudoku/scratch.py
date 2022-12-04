moves = {'p1': ['1', '5', '9', '3', '2'], 'p2': ['3', '4', '6', '7']}
solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]

for p in moves:
	for solution in solutions:
		if (
			str(solution[0]) in moves[p] and
			str(solution[1]) in moves[p] and
			str(solution[2]) in moves[p]
		):
			print("match")
			print(solution)
			print(moves[p])