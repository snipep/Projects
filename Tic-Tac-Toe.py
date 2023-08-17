board = [' ' for _ in range(10)]

def insertelement(letter, pos):
    board[pos] = letter

def isSpaceFree(pos):
    if board[pos] == ' ':
        return True
    return False

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')    
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' |' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    return True

def isWinner(board, l):
    return (board[1] == l and board[2] == l and board[3] == l) or (board[4] == l and board[5] == l and board[6] == l) or (board[7] == l and board[8] == l and board[9] == l) or (board[1] == l and board[4] == l and board[7] == l) or (board[2] == l and board[5] == l and board[8] == l) or (board[3] == l and board[6] == l and board[9] == l) or (board[1] == l and board[5] == l and board[9] == l) or (board[3] == l and board[5] == l and board[7] == l)
            
def PlayerMove():
    run = True
    move = input("Pls select the position to enter X b/w 1 to 9: ")
    while run:
        try:
            move = int(move)
            if 0 < move < 10:
                if isSpaceFree(move):
                    run = False
                    insertelement('X', move)
                else:
                    print("Sorry the Space is already occupied")
            else:
                print("Pls enter value from 1 to 9")

        except:
            print("Pls enter integer value")
            break
    
def ComputerMove():
    possibleMoves = [ x for x ,letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O' , ' X']:
        for i in possibleMoves:
            copyBoard = board[:]
            copyBoard[i] = let
            if isWinner(copyBoard, let):
                move = i
                return move
    
    # for corner moves
    corner = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corner.append(i)
    
    if len(corner) > 0:
        move = selectRandom(corner)
        return move
    
    # for mid value
    if 5 in possibleMoves:
        move = 5
        return 5

    # for edges in boards
    edge = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edge.append(i)
    
    if len(edge)  > 0:
        move = selectRandom(edge)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print("Welcome to Tic-Tac-toe")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            PlayerMove()
            printBoard(board)
        else:
            print("Sorry, You Loose")
            break
        
        if not(isWinner(board, 'X')):
            move = ComputerMove()
            if move == 0:
                print(" ")
            else:
                insertelement('O', move)
                print("The computer has places O in position ", move, ": ")
                printBoard(board)
        else:
            print("You Win!")
            break
    
    if isBoardFull(board):
        print("Tie Game")

while True:
    x = input("Do you want to play? (y/n): ")
    if x.lower() == 'y':
        board = [' ' for _ in range(10)]
        print("------------------------")
        main()
    else:
        break