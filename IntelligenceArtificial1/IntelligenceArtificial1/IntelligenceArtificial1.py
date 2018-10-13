##Global Constants
WIDTH = 5
HEIGHT = 5

def main():
    pos = make_pos(1,0)
    print(pos)
    pos_a = pos_l(pos)
    print(pos_a)


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
    for l in range(len(board)) :
        for c in range(len(board[l])) :

            # LEFT to RIGHT
            if (c + 2 ) < N :
                if is_peg(board[l][c]) and is_peg(board[l][c + 1]) and is_empty(board[l][c + 2]) :
                    addSolutionFound(make_pos(l, c), make_pos(1, c + 2), listSolutionFound)

            # RIGHT to LEFT
            if (c - 2 ) < 0 :
                if is_peg(board[l][c]) and is_peg(board[l][c - 1]) and is_empty(board[l][c - 2]) :
                    addSolutionFound(make_pos(l, c), make_pos(l, c - 2), listSolutionFound)

            # TOP to BOTTOM
            if (l + 2 ) < M :
                if is_peg(board[l][c]) and is_peg(board[l + 1][c]) and is_empty(board[l + 2][c]) :
                    addSolutionFound(make_pos(l, c), make_pos(l + 2, c), listSolutionFound)

            # BOTTOM to TOP
            if (l - 2 ) < 0 :
                if is_peg(board[l][c]) and is_peg(board[l - 1][c]) and is_empty(board[l - 2][c]) :
                    addSolutionFound(make_pos(l, c), make_pos(l - 2, c), listSolutionFound)

    return listSolutionFound

def addSolutionFound(initialPos, finalPos, listSolutionFound) :
    solutionFound = make_move(initialPos, finalPos)
    listSolutionFound.append(solutionFound)

def board_perform_move(board, move) :
      new_board = board.copy();

      l_middle_pos = abs(move[0][0] - move[1][0])
      c_middle_pos = abs(move[0][1] - move[1][1])
      middle_pos = make_pos(l_middle_pos, c_middle_pos)

      #the ball in the original position moves
      new_board[move[0][0]][move[0][1]] = c_empty()
      #the ball is now in the final position
      new_board[move[1][0]][move[1][1]] = c_peg()
      #the other ball that was between the positions disapear
      new_board[middle_pos[0]][middle_pos[1]] = c_empty()

      return new_board

main()


    







            
    
