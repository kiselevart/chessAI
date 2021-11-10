def chessboard (mode):
    board = [['e']*8 for i in xrange(8)]
    if mode = 'empty':
        return board
    elif mode = 'full':
        board[1] = 'p'
        board[6] = 'p'
        return board

chessboard('full')