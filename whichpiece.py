from board import chessboard
from coordinate import ycoord, xcoord
from gamedata import move
yco = ycoord(move)
xco = xcoord(move)

def whichknight(move):
    possibleposition = ['']*8
    board = chessboard()
    counter = 0
    if 'N' in board[yco+1][xco+2]:
        possibleposition[0] = board[yco+1][xco+2]

    if 'N' in board[yco+1][xco-2]:
        possibleposition[1] = board[yco+1][xco-2]

    if 'N' in board[yco-1][xco+2]:
        possibleposition[2] = board[yco-1][xco+2]

    if 'N' in board[yco-1][xco-2]:
        possibleposition[3] = board[yco-1][xco-2]

    if 'N' in board[yco+2][xco-1]:
        possibleposition[4] = board[yco+2][xco-1]

    if 'N' in board[yco+2][xco+1]:
        possibleposition[5] = board[yco+2][xco+1]

    if 'N' in board[yco-2][xco-1]:
        possibleposition[6] = board[yco-2][xco-1]

    if 'N' in board[yco-2][xco+1]:
        possibleposition[7] = board[yco-2][xco+1]
    
    for x in range(8):
        if possibleposition[x] != '':
            index = x
            counter += 1
    
    if counter >1:
        for x in range(8):
            if move[1] in possibleposition[x]:
                return possibleposition[x]
    else:
        return possibleposition[index]
