import copy
from search import (
    Problem
)

def main():
    print(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).result(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]),[(3, 0), (3, 2)]).board)

class solitaire(Problem) :
 """Models a Solitaire problem as a satisfaction problem.
 A solution cannot have more than 1 peg left on the board."""
 def __init__(self, board):
    """The board is a 2 dimensional array/list whose state is specified by string caracter"""
    self.initial = sol_state(board)

 def actions(self, state):
    """The list of possible moves, from the state of a board"""
    return board_moves(state.board)
 
 def result(self, state, action):
    new_board = board_perform_move(state.board, action)
    return sol_state(new_board)

 def goal_test(self, state):
    return isGoalReached(state.board)

 def path_cost(self, c, state1, action, state2):
    return c + 1

 def h(self, node):
    raise NotImplementedError

class sol_state :
    def __init__(self, board) :
        """The board is a 2 dimensional array whose state is specified by string caracter"""
        self.board = board
        self.n = len(board)
        assert self.n > 0
        self.m = len(board[0])
        assert self.m > 0
    def __lt__(self, sol_state):
        return sol_state.board < sol_state.board


# TAI content
def c_peg () :
    return "O"
def c_empty () :
    return "_"
def c_blocked () :
    return "X"
def is_empty (e) :
    return e == c_empty()
def is_peg (e) :
    return e == c_peg()
def is_blocked (e) :
    return e == c_blocked ()

# TAI pos
# Tuplo (l, c)
def make_pos (l, c) :
    return (l, c)
def pos_l (pos) :
    return pos[0]
def pos_c (pos) :
    return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f) :
    return [i, f]
def move_initial (move) :
    return move[0]
def move_final (move) :
    return move [1]

# TAI board
# Lista [Lista_l [c]]
def board_moves (board) :
    listSolutionFound = []
    N = len(board)
    M = len(board[0])
    for l in range(N) :
        for c in range(M) :

            # RIGHT to LEFT
            if (c - 2) >= 0 :
                if is_peg(board[l][c]) and is_peg(board[l][c - 1]) and is_empty(board[l][c - 2]) :
                    addSolutionFound(make_pos(l, c), make_pos(l, c - 2), listSolutionFound)

            # LEFT to RIGHT
            if (c + 2) < M :
                if is_peg(board[l][c]) and is_peg(board[l][c + 1]) and is_empty(board[l][c + 2]) :
                    addSolutionFound(make_pos(l, c), make_pos(l, c + 2), listSolutionFound)

            # BOTTOM to TOP
            if (l - 2) >= 0 :
                if is_peg(board[l][c]) and is_peg(board[l - 1][c]) and is_empty(board[l - 2][c]) :
                    addSolutionFound(make_pos(l, c), make_pos(l - 2, c), listSolutionFound)

            # TOP to BOTTOM
            u = len(board)
            if (l + 2) < N :
                if is_peg(board[l][c]) and is_peg(board[l + 1][c]) and is_empty(board[l + 2][c]) :
                    addSolutionFound(make_pos(l, c), make_pos(l + 2, c), listSolutionFound)

    return listSolutionFound

def addSolutionFound(initialPos, finalPos, listSolutionFound) :
    solutionFound = make_move(initialPos, finalPos)
    listSolutionFound.append(solutionFound)

#TAI List[List[c]]
def board_perform_move(board, move) :
      new_board = copy.deepcopy(board)

      l_middle_pos = int (((move[0][0] + move[1][0]) / 2))
      c_middle_pos = int (((move[0][1] + move[1][1]) / 2))
      middle_pos = make_pos(l_middle_pos, c_middle_pos)

      #the ball in the original position moves
      new_board[move[0][0]][move[0][1]] = c_empty()
      #the ball is now in the final position
      new_board[move[1][0]][move[1][1]] = c_peg()
      #the other ball that was between the positions disapear
      new_board[middle_pos[0]][middle_pos[1]] = c_empty()

      return new_board

#TAI boolean
def isGoalReached(board):
  #The goal is reached when there is only one peg left on the board
  count = 0
  for l in range(len(board)) :
      for c in range(len(board[0])) :
          if is_peg(board[l][c]):
              count += 1
              if count > 1:
                return False
      else: # The count must be 1
              return True 

main()


    







            
    

