from examples import *

def display_grid(grid):
	length = len(grid)*len(grid) + 2
	hbar = ""
	result = []	
	for i in range(0, length):
		hbar += "-"
	result.append([hbar])
	
	for row in grid:
		rowstring = "|"
		for i in row:
			if(i == '.'):
				rowstring +="   "
			else:
				rowstring += " " + str(i) + " "
		rowstring += "|"
		result.append([rowstring])
	result.append([hbar])	
	return result

def display_puzzle(puzzle):
	total1 = [ [], [], [], [], []]
	total2 = [ [], [], [], [], []]
	total3 = [ [], [], [], [], []]
	for grid in puzzle[0]:
		result = display_grid(grid)
		total1[0] += result[0]
		total1[1] += result[1]
		total1[2] += result[2]
		total1[3] += result[3]
		total1[4] += result[4]
	for grid in puzzle[1]:
		result = display_grid(grid)
		total2[0] += result[0]
		total2[1] += result[1]
		total2[2] += result[2]
		total2[3] += result[3]
		total2[4] += result[4]
	for grid in puzzle[2]:
		result = display_grid(grid)
		total3[0] += result[0]
		total3[1] += result[1]
		total3[2] += result[2]
		total3[3] += result[3]
		total3[4] += result[4]

	print(' '.join(total1[0]))
	print(' '.join(total1[1]))
	print(' '.join(total1[2]))
	print(' '.join(total1[3]))
	print(' '.join(total1[4]))
	print(' '.join(total2[0]))
	print(' '.join(total2[1]))
	print(' '.join(total2[2]))
	print(' '.join(total2[3]))
	print(' '.join(total2[4]))
	print(' '.join(total3[0]))
	print(' '.join(total3[1]))
	print(' '.join(total3[2]))
	print(' '.join(total3[3]))
	print(' '.join(total3[4]))



