#import the current chessboard
from board import chessboard
from coordinate import xcoord, ycoord, xcoordpt
from movetype import movetype
from movepiece import movepiece
from whichpiece import whichknight
from locatepiece import locatepiece
from gamedata import move,turn


board = chessboard()
xco = xcoord(move)
yco = ycoord(move)
movet = movetype(move)


def pawnmove(move):
    if turn == 'white':
        if 'takes' in movet:
            if board[yco][xco] == '---' and 'pb' in board[yco-1][xco]: #en passant
                movepiece(yco-1,xcoordpt(move),yco,xco,board)
                board[yco-1][xco] = '---'
            else:
                movepiece(yco-1,xcoordpt(move),yco,xco,board)
                
        else:
            if board[yco-1][xco] == 'pw-':
                movepiece(yco-1,xco,yco,xco,board)
            else:
                movepiece(yco-2,xco,yco,xco,board)
    else:
        if 'takes' in movet:
            if board[yco][xco] == '---' and 'pw' in board[yco+1][xco]: #en passant
                movepiece(yco+1,xcoordpt(move),yco,xco,board)
                board[yco+1][xco] = '---'
            else:
                movepiece(yco+1,xcoordpt(move),yco,xco,board)
                
        else:
            if board[yco+1][xco] == 'pb-':
                movepiece(yco+1,xco,yco,xco,board)
            else:
                movepiece(yco+2,xco,yco,xco,board)

    return board

def knightmove(move):
    knightindex = whichknight(move)
    knightcoord = locatepiece(knightindex)

    movepiece(knightcoord[0],knightcoord[1],yco,xco,board)
    return board
        



    

