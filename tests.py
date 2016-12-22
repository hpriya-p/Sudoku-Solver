
import unittest

class Testupdate(unittest.TestCase):
	def test_grid(self):
		test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		self.assertEqual(update_grid(test1, 0, 0, 3), [[3, 2, 3], [4, 5, 6], [7, 8, 9]])

	def test_grid_copying(self):
		test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		newtest1 = update_grid(test1, 0, 0, 4)
		newtest2 = update_grid(test1, 2, 2, 5)
		self.assertEqual(newtest1, [ [4, 2, 3], [4, 5, 6], [7, 8, 9]])
		self.assertEqual(newtest2, [ [1, 2, 3], [4, 5, 6], [7, 8, 5]])
	def test_find_solution(self):
		solution = find_solution(unsolvedSudokuPuzzle)
		self.assertEqual(solution[-1], solvedSudokuPuzzle)
if __name__ == '__main__':
	unittest.main()

