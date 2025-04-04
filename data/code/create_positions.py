import json
from getmoveschessdotcom import getMoves

def legalRookMove(positions, revPos, target, piece, take):
    if take and target.upper() not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False

    if positions[piece][0][0] == target[0].upper():
        if positions[piece][0][1] < target[1]:
            start = eval(positions[piece][0][1])
            end = eval(target[1])
        elif positions[piece][0][1] > target[1]:
            end = eval(positions[piece][0][1])
            start = eval(target[1])
        else:
            return False
        
        for i in range(start+1, end):
            if target[0].upper()+str(i) in revPos.keys():
                return False
        
        return True
    
    elif positions[piece][0][1] == target[1]:
        if positions[piece][0][0] > target[0].upper():
            start = ord(positions[piece][0][1])
            end = ord(target[1])
        elif positions[piece][0][0] < target[0].upper():
            end = ord(positions[piece][0][1])
            start = ord(target[1])
        else:
            return False

        for i in range(start+1, end):
            if chr(i)+target[1] in revPos.keys():
                return False
        
        return True

    else:
        return False

def legalKnightMove(positions, revPos, target, piece, take):
    if take and target.upper() not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False
    
    # print(ord(positions[piece][0][0], ord(target[0].upper()), eval(positions[piece][0][1]), eval(target[1])))

    if abs(ord(positions[piece][0][0]) - ord(target[0].upper())) == 2 and abs(eval(positions[piece][0][1]) - eval(target[1])) == 1:
        return True
    if abs(ord(positions[piece][0][0]) - ord(target[0].upper())) == 1 and abs(eval(positions[piece][0][1]) - eval(target[1])) == 2:
        return True

    return False

def legalBishopMove(positions, revPos, target, piece, take):
    target = target.upper()
    if take and target not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False

    # print(ord(positions[piece][0][0]), eval(positions[piece][0][1]), ord(target[0]), eval(target[1]))
    
    if abs(ord(positions[piece][0][0]) + eval(positions[piece][0][1])) != abs(ord(target[0]) + eval(target[1])):
        if abs(ord(positions[piece][0][0]) - eval(positions[piece][0][1])) != abs(ord(target[0]) - eval(target[1])):
            return False
        
    if positions[piece][0][0] > target[0]:
        (start1, mov1) = (ord(positions[piece][0][0]), -1)
    elif positions[piece][0][0] < target[0]:
        (start1, mov1) = (ord(positions[piece][0][0]), +1)
    else:
        return False

    if positions[piece][0][1] > target[1]:
        (start2, mov2) = (ord(positions[piece][0][1]), -1)
    elif positions[piece][0][1] < target[1]:
        (start2, mov2) = (ord(positions[piece][0][1]), +1)
    else:
        return False
    
    # print(start1, mov1, start2, mov2, type(mov2), type(start1), type(start2))

    for i in range(start1, ord(target[0])):
        if (chr(i)+str(start2+(i*mov2))) in revPos.keys():
            return False
        
    return True
    
def legalQueenMove(positions, revPos, target, piece, take):
    target = target.upper()
    if take and target not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False
    
    #RookCheck
    if positions[piece][0][0] == target[0].upper():
        # print('here1')
        if positions[piece][0][1] < target[1]:
            # print('here2')
            start = eval(positions[piece][0][1])
            end = eval(target[1])
        elif positions[piece][0][1] > target[1]:
            # print('here3')
            end = eval(positions[piece][0][1])
            start = eval(target[1])
        else:
            return False
        
        for i in range(start+1, end):
            if target[0].upper()+str(i) in revPos.keys():
                return False
        
        return True
    
    elif positions[piece][0][1] == target[1]:
        if positions[piece][0][0] > target[0].upper():
            start = ord(positions[piece][0][1])
            end = ord(target[1])
        elif positions[piece][0][0] < target[0].upper():
            end = ord(positions[piece][0][1])
            start = ord(target[1])
        else:
            return False

        for i in range(start+1, end):
            if chr(i)+target[1] in revPos.keys():
                return False
        
        return True
    

    #BishopCheck
    if abs(ord(positions[piece][0][0]) + eval(positions[piece][0][1])) != abs(ord(target[0]) + eval(target[1])):
        if abs(ord(positions[piece][0][0]) - eval(positions[piece][0][1])) != abs(ord(target[0]) - eval(target[1])):
            return False
        
    if positions[piece][0][0] > target[0]:
        (start1, mov1) = (ord(positions[piece][0][0]), -1)
    elif positions[piece][0][0] < target[0]:
        (start1, mov1) = (ord(positions[piece][0][0]), +1)
    else:
        return False

    if positions[piece][0][1] > target[1]:
        (start2, mov2) = (ord(positions[piece][0][1]), -1)
    elif positions[piece][0][1] < target[1]:
        (start2, mov2) = (ord(positions[piece][0][1]), +1)
    else:
        return False
    

    for i in range(start1, ord(target[0])):
        if (chr(i)+str(start2+(i*mov2))) in revPos.keys():
            return False
        
    return True

def legalKingMove(positions, revPos, target, piece, take):
    target = target.upper()
    if take and target not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False
    
    if abs(ord(positions[piece][0][0]) - ord(target[0])) == 1 and abs(eval(positions[piece][0][1]) - eval(target[1])) == 1:
        return True

    return False
    
def legalPawnMove(positions, revPos, target, piece, take, en_passant):
    target = target.upper()
    if not take and target in revPos.keys():
        # print('check1')
        return False, -1
    
    if(eval(positions[piece][0][1]) == 2 or eval(positions[piece][0][1]) == 7) and abs(eval(positions[piece][0][1]) - eval(target[1])) == 2 and target[0] == positions[piece][0][0]:
        if (target[0]+str((eval(positions[piece][0][1]) + eval(target[1]))/2)) not in revPos.keys():
            # print('Checkdhiuwefhwjefnkj')
            return True, True
        # print('check2')
        return False, -1
    
    if not take:
        if positions[piece][0][0] == target[0]:
            if piece[0] == 'P' and eval(positions[piece][0][1]) + 1 == eval(target[1]):
                return True, -1
            if piece[0] == 'p' and eval(positions[piece][0][1]) - 1 == eval(target[1]):
                return True, -1
        # print('check3')
        return False, -1
    
    if en_passant:
        if target not in revPos.keys() and abs(positions[piece][0][0] - ord(target[0])) == 1 and abs(eval(positions[piece][0][1]) - eval(target[1])) == 1:
            return True, -1
        # print('check4')
        return False, -1
    
    if target in revPos.keys() and abs(positions[piece][0][0] - ord(target[0])) == 1 and abs(eval(positions[piece][0][1]) - eval(target[1])) == 1:
        return True, -1
    
    # print('check5')
    return False, -1
    
def legalCastling(positions, revPos, target, piece1, piece2, take, moved):
    target = target.upper()
    if take and target not in revPos.keys():
        return False
    if not take and target in revPos.keys():
        return False
    
    if piece1 in moved or piece2 in moved:
        return False
    






def findRook(positions, revPos, target, black, take):
    piece = 'R'
    if black:
        piece = 'r'

    first = 0
    second = 0
    
    if legalRookMove(positions, revPos, target, piece+'1', take):
        return 1
    if legalRookMove(positions, revPos, target, piece+'2', take):
        return 2

    return 0   

def findKnight(positions, revPos, target, black, take):
    piece = 'N'
    if black:
        piece = 'n'

    first = 0
    second = 0
    
    if legalKnightMove(positions, revPos, target, piece+'1', take):
        return 1
    if legalKnightMove(positions, revPos, target, piece+'2', take):
        return 2

    return 0   

def findBishop(positions, revPos, target, black, take):
    piece = 'B'
    if black:
        piece = 'b'

    first = 0
    second = 0
    
    if legalBishopMove(positions, revPos, target, piece+'1', take):
        return 1
    if legalBishopMove(positions, revPos, target, piece+'2', take):
        return 2

    return 0   




    return 0  



def update_positions(piece_positions, revPos, move, black, moved):
    if len(move) == 2:  # Pawn move
        piece = 'P'
        if black:
            piece = 'p'
        for key, value in piece_positions.items():
            if key.startswith(piece):  # Pawn keys
                a, b = legalPawnMove(piece_positions, revPos, move, key, 0, en_passant_key)
                if a:
                    # print('AHAAAA', key)
                    value[0] = move.upper()  # Update position
                    if b:
                        en_passant = 1
                    else:
                        en_passant = 0
                    return piece_positions
        return 0
        
    elif len(move) == 3 and move[1].islower():  # Simple piece move (e.g., Bg2)
        piece = move[0].lower()
        if not black:
            piece = piece.upper()
        target = move[1:].upper()   

        if (piece == 'K' or piece == 'k') and legalKingMove(piece_positions, revPos, target, piece, 0):
            piece_positions[piece][0] = target
            if piece not in moved:
                moved.append(piece)
            return piece_positions
        
        if (piece == 'Q' or piece == 'q') and legalQueenMove(piece_positions, revPos, target, piece, 0):
            piece_positions[piece][0] = target
            return piece_positions
        

        if piece == 'R' or piece == 'r':
            num = findRook(piece_positions, revPos, target, black, 0)
            if piece not in moved:
                moved.append(piece)
        elif piece == 'B' or piece == 'b':
            num = findBishop(piece_positions, revPos, target, black, 0)
        elif piece == 'N' or piece == 'n':
            num = findKnight(piece_positions, revPos, target, black, 0)

        if num != 0:
            piece_positions[piece+str(num)][0] = target
            return piece_positions

        return 0

    elif "x" in move:
        target = move.split("x")[1].upper()

        for key, value in piece_positions.items():
            if value[0] == target:
                del piece_positions[key]
                break
        
        piece = move[0]
        if piece.islower():
            for key, value in piece_positions.items():
                if (key.startswith('p') or key.startswith('P')) and piece_positions[key][0][0].lower() == piece:  # Pawn keys
                    a, b = legalPawnMove(piece_positions, revPos, move, key, 0, en_passant)
                    if a:
                        value[0] = move.upper()  # Update position
                        if b:
                            en_passant = 1
                        else:
                            en_passant = 0
                        return piece_positions
            
            return 0

        if black:
            piece_type = piece_type.lower()

        if (piece == 'K' or piece == 'k') and legalKingMove(piece_positions, revPos, move, piece, 0):
            piece_positions[piece] = target
            if piece not in moved:
                moved.append(piece)
            return piece_positions
        
        if (piece == 'Q' or piece == 'q') and legalQueenMove(piece_positions, revPos, move, piece, 0):
            piece_positions[piece] = target
            return piece_positions
        

        if piece == 'R' or piece == 'r':
            num = findRook(piece_positions, revPos, target, black, 1)
            if piece not in moved:
                moved.append(piece)
        elif piece == 'B' or piece == 'b':
            num = findBishop(piece_positions, revPos, target, black, 1)
        elif piece == 'N' or piece == 'n':
            num = findKnight(piece_positions, revPos, target, black, 1)

        if num != 0:
            piece_positions[piece+str(num)] = target
            return piece_positions
    
    if move[-1] == '+':
        check = 1

    return 0

def getPositions(moves):
    with open("data/positions/initial.json", "r") as file:
        initial_positions = json.load(file)


    positions = [initial_positions]
    moved = []
    # Reverse dictionary for easy lookup of piece by position
    revPos = {details[0]: piece for piece, details in initial_positions.items()}
    print('INITIAL')
    print(initial_positions)
    print(revPos,'\n\n')

    for i in range(len(moves)):
        print('MOVE:', moves[i])
        output = update_positions(positions[-1], revPos, moves[i], i%2, moved)
        if output != 0:
            revPos = {details[0]: piece for piece, details in output.items()}
            print(output)
            print(revPos,'\n\n')
            positions.append(output)
        else:
            print('Wrong')
            print(moves[i])
            print(positions[-1])

    # print(legalKnightMove(initial_positions, revPos, 'f6', 'n2', 0))

    return positions
    

en_passant_key = 0
check = 0
moves = getMoves('m1')
print(getPositions(moves))
