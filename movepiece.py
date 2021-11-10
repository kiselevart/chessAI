def movepiece(pyco,pxco,yco,xco,board):
       tempboard = board[pyco][pxco]
       board[yco][xco] = tempboard
       board[pyco][pxco] = '---'