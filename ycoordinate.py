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