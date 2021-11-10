from board import chessboard

def locatepiece(piece):
    board = chessboard()
    for y in range(8):
        for x in range(8):
            if board[y][x] == piece:
                return [y,x]

print(locatepiece('Nb2'))