from copy import deepcopy
"""
a Row is a (listof (Anyof Num)) 
a Grid is a (listof Row)
a Puzzle is a (listof (listof Grid))
"""

	
def update_row(row, index, value):
	result = row[:]
	result[index] = value
	return result

def update_grid(grid, grid_row, grid_column, value):
	row = grid[grid_row]
	newrow = update_row(row, grid_column, value)
	result = deepcopy(grid)
	result[grid_row] = newrow
	return result

def update_puzzle(puzzle, puzzle_row, puzzle_col, grid_row, grid_col, val):
	logrid = puzzle[puzzle_row]
	grid = logrid[puzzle_col]
	newgrid = update_grid(grid, grid_row, grid_col, val)
	newlogrid = deepcopy(logrid)	
	newlogrid[puzzle_col] = newgrid
	newpuzzle = deepcopy(puzzle)
	newpuzzle[puzzle_row] = newlogrid
	return newpuzzle


def blank_spot_grid(grid):
                grid_row = 0
                for row in grid:
                        if ('.' in row):
                                grid_col = row.index('.')
                                return [grid_row, grid_col]
                        else:
                                grid_row += 1
def first_blank_spot (puzzle):
	puzzle_row = 0
	puzzle_col = 0				
	for list_of_grids in puzzle:
		for grid in list_of_grids:
			temp = blank_spot_grid(grid)
			if (type(temp) is list):
				puzzle_col = list_of_grids.index(grid)
				puzzle_row = puzzle.index(list_of_grids)
				return [puzzle_row, puzzle_col] + temp	
	return False

def numbers_played_row (puzzle, puzzle_row, grid_row):
	temp = []
	listofgrids = puzzle[puzzle_row]
	for grid in listofgrids:
		temp+= grid[grid_row]
	result = [x for x in temp if x != '.']
	return result


def numbers_played_col (puzzle, puzzle_col, grid_col):
	temp = []
	listofgrids = []
	for gridrow in puzzle:
		listofgrids.append(gridrow[puzzle_col])
	for grid in listofgrids:
		for row in grid:
			temp.append(row[grid_col])
	result = [x for x in temp if x != '.']
	return result 

def numbers_played_grid (puzzle, puzzle_row, puzzle_col):
	gridrow = puzzle[puzzle_row]
	grid = gridrow[puzzle_col]
	temp = []
	for row in grid:
		temp += row
	result = [x for x in temp if x != '.']
	return result

def valid_moves (puzzle, puzzle_row, puzzle_col, grid_row, grid_col):
	invalid_by_row = numbers_played_row(puzzle, puzzle_row, grid_row)
	invalid_by_col = numbers_played_col(puzzle, puzzle_col, grid_col)
	invalid_by_grid = numbers_played_grid(puzzle, puzzle_row, puzzle_col)
	invalid_rc = invalid_by_row + [x for x in invalid_by_col if x not in invalid_by_row]
	total_invalid = invalid_rc + [x for x in invalid_by_grid if x not in invalid_rc]
	valid = [x for x in range(1, 10) if x not in total_invalid]
	return valid

print (valid_moves(unsolvedSudokuPuzzle, 0, 0, 0, 0))

def neighbours (puzzle):
	coordinates = first_blank_spot(puzzle)
	puzzle_row = coordinates[0]
	puzzle_col = coordinates[1]
	grid_row = coordinates[2]
	grid_col = coordinates[3]
	
	neighbours = []
	moves = valid_moves(puzzle, puzzle_row, puzzle_col, grid_row, grid_col)
	for i in moves:
		temp =  update_puzzle(puzzle, puzzle_row, puzzle_col, grid_row, grid_col, i)
		neighbours.append(temp)
	return neighbours



def find_solution(puzzle):
	next_blank = first_blank_spot(puzzle)
	if (next_blank == False):
		return [puzzle]
	else:
		neighbour = neighbours(puzzle)
		route = find_solution_list(neighbour)
		if (route == False):
			return False
		else:
			return puzzle + route

def find_solution_list(listofpuzzles):
	if (len(listofpuzzles) == 0):
		return False
	else:
		route  = find_solution(listofpuzzles[0])
		if(route == False):
			return find_solution_list(listofpuzzles[1:])
		else:
			return route
		


