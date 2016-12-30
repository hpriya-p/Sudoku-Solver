from copy import deepcopy
from display import *
from examples import *
"""
a Puzzle is a (listof (listof Grid)) under the following conditions:
	* every (listof Grid) in Puzzle is of the same length
	* len(Puzzle) = len(listof Grid)
	* All number elements in Puzzle are a natural number 
		between 0 and (len(Puzzle))^2 inclusive 

a Grid is a (listof Row)

a Row is a (listof (Anyof Nat, '.'))  
 
"""
"""
solve_sudoku(puzzle) prints the solution to a given sudoku puzzle
solve_sudoku: Puzzle -> None
"""

def solve_sudoku(puzzle):
	display_puzzle(puzzle)
	solution = find_solution(puzzle)
	print("Solution:")
	display_puzzle(solution[-1])

"""
update_row(row, index, value) returns a copy of row by replacing the element in
	 the specified index with value. 
update_row: Row, Nat, (Anyof Char, Nat) -> Row
Requires: index < len(row)
"""
	
def update_row(row, index, value):
	if(index >= len(row)):
		raise ValueError
	else:
		result = row[:]
		result[index] = value
		return result


"""
update_grid(grid, grid_row, grid_column, value) returns a copy of grid by 
	 replacing the element in the specified row (grid_row) and column
	 (grid_column) with value. 
update_grid: Grid, Nat, Nat, (Anyof Char, Nat) -> Grid
Requires: grid_row, grid_column < len(grid)
"""
def update_grid(grid, grid_row, grid_column, value):
	row = grid[grid_row]
	newrow = update_row(row, grid_column, value)
	result = deepcopy(grid)
	result[grid_row] = newrow
	return result


"""
update_puzzle(puzzle, puzzle_row, puzzle_col, grid_row, grid_col, value) 
	returns a copy of puzzle by replacing the element in the specified
	row (grid_row) and column (grid_column) in the specified grid 
	(specified by puzzle_row and puzzle_col) with value. 
update_puzzle: Puzzle, Nat, Nat, Nat, Nat, (Anyof Char, Nat) -> Puzzle
Requires: puzzle_row, puzzle_col, grid_row, grid_column < len(puzzle)
"""

def update_puzzle(puzzle, puzzle_row, puzzle_col, grid_row, grid_col, val):
	logrid = puzzle[puzzle_row]
	grid = logrid[puzzle_col]
	newgrid = update_grid(grid, grid_row, grid_col, val)
	newlogrid = deepcopy(logrid)	
	newlogrid[puzzle_col] = newgrid
	newpuzzle = deepcopy(puzzle)
	newpuzzle[puzzle_row] = newlogrid
	return newpuzzle


"""
number_not_blank_grid(grid) returns the total number of elements in a given
	grid which are not blank ('.')
number_not_blank_grid: Grid -> Nat
"""
def number_not_blank_grid(grid):
	not_blanks = 0	
	for row in grid:
		if ('.' not in row):
			not_blanks += len(row)
		else:
			lonotblank = [x for x in row if x != '.']
			not_blanks += len(lonotblank)
	return not_blanks


"""
select_grid(puzzle) returns the coordinates of the grid in the puzzle with the
	fewest blanks ('.')
select_grid: Puzzle -> (listof Nat)
"""
 
def select_grid(puzzle):
	max_not_blanks = 0
	puzzle_row = 0
	puzzle_col = 0
	for list_of_grids in puzzle:
		for grid in list_of_grids:
			grid_not_blanks = number_not_blank_grid(grid)
			if ((grid_not_blanks > max_not_blanks) and (grid_not_blanks < len(grid) * len(grid))):
				max_not_blanks = grid_not_blanks
				puzzle_col = list_of_grids.index(grid)
				puzzle_row = puzzle.index(list_of_grids)
	logrid = puzzle[puzzle_row]
	grid = logrid[puzzle_col]
	blank_spot = blank_spot_grid(grid)
	try:
		return [puzzle_row, puzzle_col] + blank_spot	
	except TypeError:
		return False		


"""
blank_spot_grid(grid) returns the coordinates of the first blank spot in grid
blank_spot_grid: Grid -> (listof Nat)
"""					

def blank_spot_grid(grid):
                grid_row = 0
                for row in grid:
                        if ('.' in row):
                                grid_col = row.index('.')
                                return [grid_row, grid_col]
                        else:
                                grid_row += 1


"""
numbers_played_row(puzzle, puzzle_row, grid_row) returns a list of all numbers
	in the row of the puzzle
numbers_played_row: Puzzle, Nat, Nat -> (listof Nat)
"""
def numbers_played_row (puzzle, puzzle_row, grid_row):
	temp = []
	listofgrids = puzzle[puzzle_row]
	for grid in listofgrids:
		temp+= grid[grid_row]
	result = [x for x in temp if x != '.']
	return result


"""
numbers_played_col(puzzle, puzzle_col, puzzle_row) returns a list of all
	numbers in the column of the puzzle
numbers_played_row: Puzzle, Nat, Nat -> (listof Nat)
"""
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


"""
numbers_played_grid(puzzle, puzzle_row, puzzle_col) returns a list of all
	numbers in the specified grid
numbers_played_grid: Puzzle, Nat, Nat -> (listof Nat)
"""

def numbers_played_grid (puzzle, puzzle_row, puzzle_col):
	gridrow = puzzle[puzzle_row]
	grid = gridrow[puzzle_col]
	temp = []
	for row in grid:
		temp += row
	result = [x for x in temp if x != '.']
	return result

"""
valid_moves(puzzle, puzzle_row, puzzle_col, grid_row, grid_col) returns all 
	valid moves for a given puzzle, and coordinates for a specific element
	where the new number will be placed. 
valid_moves: Puzzle, Nat, Nat, Nat, Nat -> (listof Puzzle)
"""
def valid_moves (puzzle, puzzle_row, puzzle_col, grid_row, grid_col):
	invalid_by_row = numbers_played_row(puzzle, puzzle_row, grid_row)
	invalid_by_col = numbers_played_col(puzzle, puzzle_col, grid_col)
	invalid_by_grid = numbers_played_grid(puzzle, puzzle_row, puzzle_col)
	invalid_rc = invalid_by_row + [x for x in invalid_by_col if x not in invalid_by_row]
	total_invalid = invalid_rc + [x for x in invalid_by_grid if x not in invalid_rc]
	length = len(puzzle)
	maxval = length*length + 1
	valid = [x for x in range(1, maxval) if x not in total_invalid]
	return valid

"""
neighbours(puzzle) returns a list of all neighbours of a given node
neighbours: Puzzle -> (listof Puzzle)
"""
def neighbours (puzzle):
	coordinates = select_grid(puzzle)
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


"""
find_solution(puzzle) returns the solution to a given sudoku puzzle
find_solution: Puzzle -> (listof Puzzle)
"""
def find_solution(puzzle):
	next_blank = select_grid(puzzle)
	if (next_blank == False):
		return [puzzle]
	else:
		neighbour = neighbours(puzzle)
		route = find_solution_list(neighbour)
		if (route == False):
			return False
		else:
			return puzzle + route


"""
find_solution_list(listofpuzzles) returns the solution given a list of neighbours
find_solution_list: (listof Puzzle) -> (listof Puzzle)
"""
def find_solution_list(listofpuzzles):
	if (len(listofpuzzles) == 0):
		return False
	else:
		route  = find_solution(listofpuzzles[0])
		if(route == False):
			return find_solution_list(listofpuzzles[1:])
		else:
			return route
		

solve_sudoku(p1_unsolved)
