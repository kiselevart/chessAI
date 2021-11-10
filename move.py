#import the current chessboard
from board import chessboard
from xcoordinate import xcoord
from ycoordinate import ycoord
from movetype import movetype

def chessmove(move):

    board = chessboard()
    xco = xcoord(move)
    yco = ycoord(move)
    movet = movetype(move)

    tempboard = ''

    if 'pawn' in movet:
       tempboard = board[yco-1][xco]
       board[yco][xco] = tempboard
       board[yco-1][xco] = '--'
    
    return board

print(chessmove('e3'))
    

