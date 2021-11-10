#finds x coordinate of the move so e5 would give 4
from gamedata import move

def xcoord(move):
    length = len(move)

    if 'a' in move[length-2]:
        return 7
    elif 'b' in move[length-2]:
        return 6
    elif 'c' in move[length-2]:
        return 5
    elif 'd' in move[length-2]:
        return 4
    elif 'e' in move[length-2]:
        return 3
    elif 'f' in move[length-2]:
        return 2
    elif 'g' in move[length-2]:
        return 1
    elif 'h' in move[length-2]:
        return 0

def xcoordpt(move):
    if 'a' in move[0]:
        return 7
    elif 'b' in move[0]:
        return 6
    elif 'c' in move[0]:
        return 5
    elif 'd' in move[0]:
        return 4
    elif 'e' in move[0]:
        return 3
    elif 'f' in move[0]:
        return 2
    elif 'g' in move[0]:
        return 1
    elif 'h' in move[0]:
        return 0

#finds y coordinate of the move so e5 would give 5

def ycoord(move):
    move = str(move)
    if '1' in move:
        return 0
    elif '2' in move:
        return 1
    elif '3' in move:
        return 2
    elif '4' in move:
        return 3
    elif '5' in move:
        return 4
    elif '6' in move:
        return 5
    elif '7' in move:
        return 6
    elif '8' in move:
        return 7