def getMoves(filename):
    import re

    match = open('data/matches/'+filename+'.txt', 'r').read()
    moves = re.findall(r'\d+\.\s*([^\s]+)\s+([^\s]+)', match)
    moves = [move for pair in moves for move in pair]
    moves[-1] = moves[-1][:-1]

    return moves

print(getMoves('m1'))