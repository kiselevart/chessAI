#finds x coordinate of the move so e5 would give 4

def xcoord(move):
    if 'a' in move:
        return 0
    elif 'b' in move:
        return 1
    elif 'c' in move:
        return 2
    elif 'd' in move:
        return 3
    elif 'e' in move:
        return 4
    elif 'f' in move:
        return 5
    elif 'g' in move:
        return 6
    elif 'h' in move:
        return 7