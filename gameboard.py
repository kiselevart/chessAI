from move import knightmove, pawnmove
from gamedata import move

globalboard = knightmove(move)
for x in range(8):
    print(globalboard[x])