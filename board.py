def chessboard ():
    #empty space is --, pawn is p, knight is k, bishop is b, rook is r, queen is Q, king is K, w and b means white or black pieces 
    board = [['---']*8 for i in range(8)]
    x = 0
    for x in range(8):
        board[1][x] = 'pw-'
        board[6][x] = 'pb-'

    board[0][0] = 'Rw1'
    board[0][7] = 'Rw2'
    board[7][0] = 'Rb1'
    board[7][7] = 'Rb2' #initialise rooks
    
    board[0][1] = 'Nw1'
    board[0][6] = 'Nw2'
    board[7][1] = 'Nb1'
    board[7][6] = 'Nb2' #initialise knights

    board[0][2] = 'Bw1'
    board[0][5] = 'Bw2'
    board[7][2] = 'Bb1'
    board[7][5] = 'Bb2' #initialise bishops

    board[0][3] = 'Kw-'
    board[0][4] = 'Qw1'
    board[7][3] = 'Qb1'
    board[7][4] = 'Kb-' #initialise king and queens
    
    #useful code for printing it out and having it look nice: for x in range(8): print(board[x])

    return board
