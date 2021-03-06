#!/usr/bin/python3
# Grupo 094: Sergio Carvalho (81513), Nuno Silva-Pinto ()

import copy
from search import Problem, InstrumentedProblem, breadth_first_search, Node

class solitaire(Problem):
    """Models a Solitaire problem as a satisfaction problem.
    A solution is reached when only 1 peg is left on the board."""
    def __init__(self, board):
        """The board is a 2 dimensional array/list whose state is specified by string caracter"""
        self.initial = sol_state(board)

    def actions(self, state):
        """The list of possible moves, from the state of a board"""
        return board_moves(state.board)
 
    def result(self, state, action):
        return sol_state(board_perform_move(state.board, action))

    def goal_test(self, state):
        '''The goal is reached when there is only one peg left on the board'''
        return state.pegc == 1

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        return node.state.pegc

class sol_state :
    def __init__(self, board) :
        """The board is a 2 dimensional array whose state is specified by string caracter"""
        self.board = board
        self.pegc = board_peg_count(board)
    def __lt__(self, other):
        return isinstance(other, sol_state) and self.board < other.board
    def __gt__(self, other):
        return isinstance(other, sol_state) and self.board > other.board
    def __eq__(self, other):
        return isinstance(other, sol_state) and self.board == other.board
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    def __hash__(self):
        flatboard = [pos for line in self.board for pos in line]
        return hash(tuple(flatboard))

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
   #the ball in the original position moves
   new_board[move[0][0]][move[0][1]] = c_empty()
   #the other ball that was between the positions disapear
   new_board[l_middle_pos][c_middle_pos] = c_empty()
   #THE BALl is now in the final position
   new_board[move[1][0]][move[1][1]] = c_peg()
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
      and (l - 1 < 0 or not is_peg(board[l - 1][c]))\
      and (l + 1 >= N or not is_peg(board[l + 1][c]))\
      and (c + 1 >= M or not is_peg(board[l][c + 1]))\
      and (c - 1 < 0 or not is_peg(board[l][c - 1])) and 1

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
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos) :
    return pos[1]
