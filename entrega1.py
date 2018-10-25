#!/usr/bin/python3
# Grupo 094: Sergio Carvalho (81513), Nuno Silva-Pinto ()

import copy
from search import Problem, InstrumentedProblem, breadth_first_search, Node

class solitaire(Problem):
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
        '''The goal is reached when there is only one peg left on the board'''
        return board_peg_count(state.board) == 1

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        # https://stackoverflow.com/questions/6784269/peg-solitaire-senku-solution-algorithm
        # A primeira resposta e util.
        # Vou usar as duas primeiras heuristicas, com peso de 1/2 cada uma.
        n = node.state.n
        m = node.state.m
        board = node.state.board
        sucessor_c = 4 - len(board_moves(board)) # the lower the better
	# Nao sei se estas proximas heuristicas sao admissiveis.
        # Se conseguires provar que são, diz.
        #peg_c = n * m - board_peg_count(board) # the lower the better
        #isolated_c = isolated_peg_count(board) # the lower the better 
        return sucessor_c# // 3 + peg_c // 3 + isolated_c // 3

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
    def __gt__(self, sol_state):
        return sol_state.board > sol_state.board

def right_to_left(board, pos):
    l = pos_l(pos)
    c1 = pos_c(pos) # current
    c2 = c1 - 1     # middle
    c3 = c2 - 1     # target
    if c3 >= 0 and is_peg(board[l][c2]) and is_empty(board[l][c3]):
        return make_pos(l, c3)

def left_to_right(board, pos):
    M = len(board[0])
    l = pos_l(pos)
    c1 = pos_c(pos) # current
    c2 = c1 + 1     # middle
    c3 = c2 + 1     # target
    if c3 < M and is_peg(board[l][c2]) and is_empty(board[l][c3]):
        return make_pos(l, c3)

def bottom_to_top(board, pos):
    c = pos_c(pos)
    l1 = pos_l(pos) # current
    l2 = l1 - 1     # middle
    l3 = l2 - 1     # target
    if l3 >= 0 and is_peg(board[l2][c]) and is_empty(board[l3][c]):
        return make_pos(l3, c)

def top_to_bottom(board, pos):
    N = len(board)
    c = pos_c(pos)
    l1 = pos_l(pos) # current
    l2 = l1 + 1     # middle
    l3 = l2 + 1     # target
    if l3 < N and is_peg(board[l2][c]) and is_empty(board[l3][c]):
        return make_pos(l3, c)

# TAI board
# Lista [Lista_l [c]]
def board_moves (board) :
    M = len(board[0])
    N = len(board)
    listSolutionFound = []
    for l in range(N):
        for c in range(M):
            if not is_peg(board[l][c]):
                continue
            pos = make_pos(l, c)
            for f in left_to_right, right_to_left, bottom_to_top, top_to_bottom:
                newpos = f(board, pos)
                if newpos:
                    addSolutionFound(pos, newpos, listSolutionFound)
    return listSolutionFound

def addSolutionFound(initialPos, finalPos, listSolutionFound):
    solutionFound = make_move(initialPos, finalPos)
    listSolutionFound.append(solutionFound)

#TAI List[List[c]]
def board_perform_move(board, move) :
   new_board = copy.deepcopy(board)
   l_middle_pos = (move[0][0] + move[1][0]) // 2
   c_middle_pos = (move[0][1] + move[1][1]) // 2
   middle_pos = make_pos(l_middle_pos, c_middle_pos)
   #the ball in the original position moves
   new_board[move[0][0]][move[0][1]] = c_empty()
   #the ball is now in the final position
   new_board[move[1][0]][move[1][1]] = c_peg()
   #the other ball that was between the positions disapear
   new_board[middle_pos[0]][middle_pos[1]] = c_empty()
   return new_board

def board_peg_count(board):
    count = 0
    for l in range(len(board)):
        for c in range(len(board[0])):
            if is_peg(board[l][c]):
                count += 1
    return count

def isolated_peg_count(board):
    M = len(board[0])
    N = len(board)
    count = 0
    for l in range(N):
        for c in range(M):
            count += is_isolated_peg(board, make_pos(l, c)) 
    return count

def is_isolated_peg(board, pos):
   N = len(board)
   M = len(board[0])
   l = pos_l(pos)
   c = pos_c(pos)
   return is_peg(board[l][c])\
      and l - 1 <= 0 and is_peg(board[l - 1][c])\
      and l + 1 > N  and is_peg(board[l + 1][c])\
      and c + 1 <= 0 and is_peg(board[l][c + 1])\
      and c - 1 > M  and is_peg(board[l][c - 1]) and 1

#_________________________________PROFESSOR____________________________________
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

# TAI move: lista [p_initial, p_final]
def make_move (i, f) :
    return [i, f]
def move_initial (move) :
    return move[0]
def move_final (move) :
    return move[1]

# TAI pos: tuplo (l, c)
def make_pos (l, c) :
    return (l, c)
def pos_l (pos) :
    return pos[0]
def pos_c (pos) :
    return pos[1]