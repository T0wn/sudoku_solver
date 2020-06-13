import unittest
import sudoku_puzzle

class TestSudoku(unittest.TestCase):


    def test_solves(self):
        testPuzzle = [
            [0,2,0,3,4,0,0,0,1],
            [8,5,0,0,2,0,0,4,0],
            [0,0,3,0,0,1,2,5,6],
            [0,0,0,0,3,0,7,6,0],
            [0,0,4,1,6,0,5,9,0],
            [6,8,0,4,0,0,0,0,0],
            [5,0,8,0,0,3,0,0,0],
            [1,9,7,2,5,4,0,0,0],
            [0,4,2,0,0,7,9,1,0]
        ]
        solvedPuzzle = [
            [9,2,6,3,4,5,8,7,1],
            [8,5,1,7,2,6,3,4,9],
            [4,7,3,8,9,1,2,5,6],
            [2,1,9,5,3,8,7,6,4],
            [7,3,4,1,6,2,5,9,8],
            [6,8,5,4,7,9,1,3,2],
            [5,6,8,9,1,3,4,2,7],
            [1,9,7,2,5,4,6,8,3],
            [3,4,2,6,8,7,9,1,5]
        ]
        
        puzzle = sudoku_puzzle.sudoku_puzzle(puzzle=testPuzzle)
        self.assertEqual(solvedPuzzle, puzzle.solve_with_backtracking())


        testPuzzle2 = [
            [5,0,0,0,0,9,7,6,0],
            [0,0,4,0,8,0,0,1,0],
            [0,0,2,6,0,0,0,9,0],
            [0,0,0,0,0,8,0,0,0],
            [6,0,9,2,0,5,4,0,3],
            [0,0,0,4,0,0,0,0,0],
            [0,1,0,0,0,2,6,0,0],
            [0,9,0,0,4,0,5,0,0],
            [0,5,6,8,0,0,0,0,9]
        ]
        solvedPuzzle2 = [
            [5,3,8,1,2,9,7,6,4],
            [9,6,4,5,8,7,3,1,2],
            [1,7,2,6,3,4,8,9,5],
            [3,4,5,7,9,8,1,2,6],
            [6,8,9,2,1,5,4,7,3],
            [7,2,1,4,6,3,9,5,8],
            [8,1,3,9,5,2,6,4,7],
            [2,9,7,3,4,6,5,8,1],
            [4,5,6,8,7,1,2,3,9]
        ]

        puzzle = sudoku_puzzle.sudoku_puzzle(puzzle=testPuzzle2)
        self.assertEqual(solvedPuzzle2, puzzle.solve_with_backtracking())
        


if __name__ == "__main__":
    unittest.main()