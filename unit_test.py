import unittest
import IntelligenceArtificial1

boards = [
	 [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"], ["O","_","O","_","_"], ["_","O","_","_","_"]],
         [['O','_','_','O','_'], ['O','_','O','_','O'], ['_','O','_','O','_'], ['O','_','O','_','_'], ['_','O','_','_','_']]
]
	
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(board_moves(boards[0]), [[(0, 2), (0, 0)], [(0, 2), (0, 4)], [(0, 2), (2, 2)]] )

game = solitaire()
p = InstrumentedProblem(game)
resultBreadthFirstSearch = breadth_first_search(p)
print(resultBreadthFirstSearch.solution())
print(resultBreadthFirstSearch.path()[0].state.board)
