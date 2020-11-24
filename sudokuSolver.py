def validCheck(board):
    valid = checkRow(board) and checkColumn(board) and checkSquare(board)
    return valid

def checkRow(board):
    bools = []
    
    for i in range(9):
        validity = bools.append([x for x in sorted(board[i]) if x != 0] == [x for x in sorted(list(set(board[i]))) if x != 0])
    
    return all(bools)

def checkColumn(board):
    bools = []
    board = list(map(list, zip(*board)))
    
    for i in range(9):
        validity = bools.append([x for x in sorted(board[i]) if x != 0] == [x for x in sorted(list(set(board[i]))) if x != 0])
    
    return all(bools)

def checkSquare(board):
    bools = []
    boxBoard = []
    
    for j in range(3):
        for i in range(3):
            box = take(j*3,j*3+3,[x for x in sampleBoard[3*i]]) + take(j*3,j*3+3,[x for x in sampleBoard[3*i+1]]) + take(j*3,j*3+3,[x for x in sampleBoard[3*i+2]])
            boxBoard.append(box)
    
    for i in range(9):
        validity = bools.append([x for x in sorted(boxBoard[i]) if x != 0] == [x for x in sorted(list(set(boxBoard[i]))) if x != 0])

    return all(bools)

def take(n, p, tList):
    new = []
    for i in range(n):
        tList.pop(0)
    for i in range(p-n):
        new.append(tList.pop(0))
    return new

def findEmpty(board, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if board[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                return x,y
    return -1,-1

def solve(board, i=0, j=0):
    i,j = findEmpty(board, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        board[i][j] = e
        if validCheck(board):
            if solve(board, i, j):
                return True
        board[i][j] = 0
    return False

sampleBoard = [[9,0,0,8,1,0,0,0,0],\
               [0,0,5,0,0,4,7,0,6],\
               [0,0,0,2,0,5,8,0,1],\
               [0,9,0,7,4,0,5,0,0],\
               [0,0,0,0,0,3,0,7,0],\
               [7,4,0,0,0,0,0,0,0],\
               [3,0,0,9,5,0,6,0,0],\
               [0,0,6,4,0,0,0,1,3],\
               [1,7,0,0,0,0,0,0,4]]
