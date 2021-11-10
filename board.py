def chessboard ():
    #empty space is --, pawn is p, knight is k, bishop is b, rook is r, queen is Q, king is K, w and b means white or black pieces 
    board = [['--']*8 for i in range(8)]
    x = 0
    for x in range(8):
        board[1][x] = 'pb'
        board[6][x] = 'pw'

    board[0][0] = 'Rb'
    board[0][7] = 'Rb'
    board[7][0] = 'Rw'
    board[7][7] = 'Rw' #initialise rooks
    
    board[0][1] = 'Nb'
    board[0][6] = 'Nb'
    board[7][1] = 'Nw'
    board[7][6] = 'Nw' #initialise knights

    board[0][2] = 'Bb'
    board[0][5] = 'Bb'
    board[7][2] = 'Bw'
    board[7][5] = 'Bw' #initialise bishops

    board[0][3] = 'Kb'
    board[0][4] = 'Qb'
    board[7][3] = 'Qw'
    board[7][4] = 'Kw' #initialise king and queens
    
    #useful code for printing it out and having it look nice: for x in range(8): print(board[x])

    return board
