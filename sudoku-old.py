# A grid contains 9 squares, each with a digit from 1 to 9. Blank squares will be represented using the character '.'

class Grid:
	def __init__(self, row1, row2, row3):
		self.row1 = row1
		self.row2 = row2
		self.row3 = row3
	
	def getRow1 (self):
		return self.row1

	def getRow2 (self):
		return self.row2

	def getRow3 (self):
		return self.row3

	def update (self, row_num, column_num, new_val):
		if (row_num == 0):
			row = self.getRow1()
			row[column_num] = new_val
			self.row1 = row
		elif (row_num == 1):
			row = self.getRow2()
			row[column_num] = new_val
			self.row2 = row
		else:
			row = self.getRow3()
			row[column_num] = new_val
			self.row3 = row
		
	def displayGrid (self):
		r1 = self.getRow1()
		r2 = self.getRow2()
		r3 = self.getRow3()

		def lst_to_string(lst):
			string = "|"
			for i in lst:
				if (i == '.'):
					string += "   |"#"| |"
				else:
					string += " " + str(i) + " |"#"| " + str(i) + " |"

			return string
		r1_str = lst_to_string(r1)
		r2_str = lst_to_string(r2)
		r3_str = lst_to_string(r3)	
		return ["-------------", r1_str, "-------------", r2_str,"-------------", r3_str, "-------------"]

#mygrid = Grid ([1, '.', 2], [3, 4, '.'], [9, 7, 6])

#mygrid.displayGrid()


# A sudoku puzzle is made up of 9 grids, and has 3 columns (of grids) and 3 rows of grids
class puzzle:

	def __init__(self, row1, row2, row3):
		self.row1 = row1
		self.row2 = row2
		self.row3 = row3

	def getRow1 (self):
		return self.row1

	def getRow2 (self):
		return self.row2

	def getRow3 (self):
		return self.row3

	def update(self, puzzle_row, puzzle_column, grid_row, grid_col, value):
		if (puzzle_row == 0):
			row = self.getRow1()
			grid = row[puzzle_column]
			grid.update(grid_row, grid_col, value)
			row[puzzle_column] = grid
			self.row1 = row
		
		elif (puzzle_row == 1):
			row = self.getRow2()
			grid = row[puzzle_column]
			grid.update(grid_row, grid_col, value)
			row[puzzle_column] = grid
			self.row2 = row

		else:
			row = self.getRow3()
			grid = row[puzzle_column]
			grid.update(grid_row, grid_col, value)
			row[puzzle_column] = grid
			self.row3 = row


	def displayPuzzle(self):
		
		def printGridRow(row):
			str1 = ""
			str2 = ""
			str3 = ""
			str4 = ""
			str5 = ""
			str6 = ""
			str7 = ""	
			for i in row:
				str1 += i.displayGrid()[0]
				str2 += i.displayGrid()[1]
				str3 += i.displayGrid()[2]
				str4 += i.displayGrid()[3]
				str5 += i.displayGrid()[4]
				str6 += i.displayGrid()[5]
				str7 += i.displayGrid()[6]
			print (str1)
			print (str2)
			print (str3)
			print (str4)
			print (str5)
			print (str6)
			print (str7)
		printGridRow(self.getRow1())
		printGridRow(self.getRow2())
		printGridRow(self.getRow3())

grid1A = Grid(['.', 7, 1], ['.', '.', '.'], [4, 9, '.'])
grid1B = Grid(['.', 9, '.'], [3, '.', 6], ['.', '.', '.'])
grid1C = Grid([8, '.', '.'], ['.', '.', '.'], [7, '.', 5])
grid2A = Grid(['.', 1, '.'], [9, '.', 2], ['.', '.', '.'])
grid2B = Grid([9, '.', '.'], ['.', '.', '.'], ['.', '.', 8])
grid2C = Grid(['.', '.', '.'], [6, '.', 3], ['.', 2, '.'])
grid3A = Grid([8, '.', 5], ['.', '.', '.'], ['.', '.', 7])
grid3B = Grid(['.', '.', '.'], [6, '.', 7], ['.', 4, '.'])
grid3C = Grid(['.', 7, 6], ['.', '.', '.'], [3, 5, '.'])

grid1An = Grid([3, 7, 1], [5, 2, 8], [4, 9, 6])
grid1Bn = Grid([5, 9, 4], [3, 7, 6], [2, 8, 1])
grid1Cn = Grid([8, 6, 2], [1, 9, 4], [7, 3, 5])
grid2An = Grid([6, 1, 4], [9, 8, 2], [7, 5, 3])
grid2Bn = Grid([9, 2, 3], [7,1,5], [4, 6, 8])
grid2Cn = Grid([5, 8, 7], [6, 4, 3], [9, 2, 1])
grid3An = Grid([8, 4, 5], [2, 3, 9], [1, 6, 7])
grid3Bn = Grid([1, 3, 9], [6, 5, 7], [8, 4, 2])
grid3Cn = Grid([2, 7, 6], [4, 1, 8], [3, 5, 9])

unsolvedSudokuPuzzle = puzzle([grid1A, grid1B, grid1C], [grid2A, grid2B, grid2C], [grid3A, grid3B, grid3C])

solvedSudokuPuzzle = puzzle([grid1An, grid1Bn, grid1Cn], [grid2An, grid2Bn, grid2Cn], [grid3An, grid3Bn, grid3Cn])


unsolvedSudokuPuzzle.displayPuzzle()

"""
Strategy for generating neighbours: a valid number will be placed in the first blank spot. 

Required functions:
	* first-blank-spot: gives the puzzle_row, puzzle_col, grid_row, and grid_col of first blank spot 
        * numbers-already-played(row): returns all numbers that already exist in that row
        * numbers-already-played(column): returns all numbers that already exist in that column
        * valid-moves: returns a list of all valid moves for that number
        * neighbours: generates all neighbours using valid-moves

"""

def first_blank_spot (puzzle):
	def blank_in_grid (grid):
		list_of_rows = [grid.getRow1(), grid.getRow2(), grid.getRow3()]
		for row in list_of_rows:
			for i in row:
				if (i == '.'):
					return [list_of_rows.index(row), row.index(i)]
	
	for grid_row in [puzzle.getRow1(), puzzle.getRow2(), puzzle.getRow3()]:
		for grid in grid_row:
			temp = blank_in_grid(grid)
			if (type(temp) is list):
				return (temp)
				

	return False




