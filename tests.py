from examples import *
from sudoku import *
import unittest


class Testupdate(unittest.TestCase):

	def test_update_row(self):
		self.assertEqual(update_row([1, 2, 3], 2, 17), [1, 2, 17])
		with self.assertRaises(ValueError):
			update_row([1, 2, 3], 3, 4)
	def test_update_grid(self):
		test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		self.assertEqual(update_grid(test1, 0, 0, 3), [[3, 2, 3], [4, 5, 6], [7, 8, 9]])
		#with self.assertRaises(ValueError):
		#	update_grid(test1, 3, 0, 4)
		#with self.assertRaises(ValueError):
		#	update_grid(test1, 0, 3, 4)

	def test_update_puzzle(self):
		g1 = [[1, 2], [3, 4]]
		g2 = [[2, 1], [3, 4]]
		g3 = [[3, 4], [1, 2]]
		g4 = [[4, 3], [1, 2]]
		puzzle1 = [[g1, g2], [g3, g4]]
		g3new = [[3, 4], ['.', 2]]
		puzzle2 = [[g1, g2], [g3new, g4]]
		self.assertEqual(update_puzzle(puzzle1, 1, 0, 1, 0, '.'), puzzle2) 

	def test_number_not_blank_grid(self):
		test = [[1, '.', '.'], [4, '.', 6], [7, 8, 9]]
		self.assertEqual(number_not_blank_grid(test), 6)
	def test_select_grid(self):
		g1 = [['.', '.'], ['.', '.']]
		g2 = [['.', 1], [3, 4]]
		g3 = [['.', 4], ['.', 2]]
		g4 = [['.', 3], [1, 2]]
		puzzle1 = [[g1, g2], [g3, g4]]
		g5 = [[4, 3], [2, 1]]
		g6 = [['.', 1], ['.', '.']]
		g7 = [['.', 4], ['.', 2]]
		g8 = [[1, 3], ['.', 2]]
		puzzle2 = [[g5, g6], [g7, g8]]
		g9 = [['.', '.'], ['.', '.']]
		g10 = [['.', '.'], ['.', '.']]
		g11 = [['.', '.'], ['.', '.']]
		g12 = [['.', '.'], ['.', '.']]
		puzzle3 = [[g9, g10], [g11, g12]]
		ga = [[1, 2], [3, 4]]
		gb = [[2, 1], [3, 4]]
		gc = [[3, 4], [1, 2]]
		gd = [[4, 3], [1, 2]]
		puzzle4 = [[ga, gb], [gc, gd]]

		self.assertEqual(select_grid(puzzle1), [0, 1, 0, 0])
		self.assertEqual(select_grid(puzzle2), [1, 1, 1, 0])
		self.assertEqual(select_grid(puzzle3), [0, 0, 0, 0])
		self.assertEqual(select_grid(puzzle4), False) 

#	def test_find_solution_p1(self):
#		solution = find_solution(p1_unsolved)
#		self.assertEqual(solution[-1],p1_solved)
	def test_find_solution_p2(self):
		solution = find_solution(p2_unsolved)
		self.assertEqual(solution[-1], p2_solved)

	#def test_find_solution_b(self):
	#	solution = find_solution(b_unsolved)
	#	print(solution[-1])
	#	self.assertEqual(solution[-1], b_solved)
if __name__ == '__main__':
	unittest.main()

