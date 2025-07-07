"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    xcount=sum(lis.count(X) for lis in board)
    ocount=sum(lis.count(O) for lis in board)
    return X if xcount==ocount else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    else:
        res=set()
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]==EMPTY:
                    res.add((i,j))    
        return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y=action
    if x>=3 or y>=3 or x<0 or y<0:  
        raise Exception("Out of bounds!")
    elif board[x][y]!=EMPTY:
        raise Exception("Illegal Move!")
    playa=player(board)
    def deepcopy(arr):
        return [ar[:] for ar in arr]
    boardcopy=deepcopy(board)
    boardcopy[x][y]=playa
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner=None
    # horizontal check:
    for row in range(3):
        possible_winner=board[row][0]
        if possible_winner==EMPTY:
            continue
        col=0
        while col<3:
            if board[row][col]!=possible_winner or board[row][col]==EMPTY:
                break
            col+=1
        if col==3:
            winner=possible_winner
            return winner
    # vertical check:
    for col in range(3):
        possible_winner=board[0][col]
        if possible_winner==EMPTY:
            continue
        row=0
        while row<3:
            if board[row][col]!=possible_winner or board[row][col]==EMPTY:
                break
            row+=1
        if row==3:
            winner=possible_winner
            return winner
    # diagonal check :
    possible_winner=board[0][0]
    if possible_winner!=EMPTY and possible_winner==board[1][1] and possible_winner==board[2][2]:
        winner=possible_winner
        return winner
    possible_winner=board[0][2]
    if possible_winner!=EMPTY and possible_winner==board[1][1] and possible_winner==board[2][0]:
        winner=possible_winner
        return winner
    return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flag=True
    for lis in board: 
        if EMPTY in lis:
            flag=False
    if winner(board) or flag:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    currplaya=player(board)
    moves=actions(board)
    bestmove=None

    if currplaya==X:
        bestscore=-math.inf
        for move in moves: # type: ignore
            val=min_val(result(board,move))
            if val>bestscore:
                bestscore=val
                bestmove=move
    else:
        bestscore=math.inf
        for move in moves: # type: ignore
            val=max_val(result(board,move))
            if val<bestscore:
                bestscore=val
                bestmove=move
    return bestmove

def max_val(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,min_val(result(board,action)))
    return v
def min_val(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
       v=min(v,max_val(result(board,action)))
    return v