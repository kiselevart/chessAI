#function that identifies the type of common move the coordinate is e.g Nxe5 will say knighttakes, can identify castles too
from gamedata import move
def movetype(move):

    movelength = len(move)

    movetype = ''
    piece = ''
    finalstring = ''

    if 'x' in move: #finds out if takes or not
        movetype = 'takes'
    else:
        movetype = 'move'

    if 'R' in move: #finds out which chess piece
        piece = 'rook'
    elif 'N' in move:
        piece = 'knight'
    elif 'B' in move:
        piece = 'bishop'
    elif 'K' in move:
        piece = 'king'
    elif 'Q' in move:
        piece = 'queen'
    elif 'O' in move:
        piece = 'castles' 
    else: 
        piece = 'pawn' #since none of the pieces it has to be a pawn move
    
    finalstring = piece + movetype
    return finalstring