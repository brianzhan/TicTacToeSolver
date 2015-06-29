import operator
from copy import copy, deepcopy

def print_welcome_message():
    print "Welcome to the tictactoe player!"

globalBoardArray = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
takenSquaresBoard = [[0,0,0], [0,0,0], [0,0,0]]

spotNotTaken = False


def display_board(boardArray):
    print '---------------------'
    print '|     |      |      |'
    print '|  ' + boardArray[0][0] + '  |  ' + boardArray[0][1] + '   |  ' + boardArray[0][2] + '   | '
    print '---------------------'
    print '|  ' + boardArray[1][0] + '  |  ' + boardArray[1][1] + '   |  ' + boardArray[1][2] + '   | '
    print '|     |      |      |'
    print '---------------------'
    print '|  ' + boardArray[2][0] + '  |  ' + boardArray[2][1] + '   |  ' + boardArray[2][2] + '   | '
    print '|     |      |      |'
    print '---------------------'


def main():
    global hypotheticalTaken
    global hypotheticalBoard
    hypotheticalTaken = GetBoardCopy(takenSquaresBoard)
    hypotheticalBoard = GetBoardCopy(globalBoardArray)
    print_welcome_message()
    display_board(globalBoardArray)
    while (gameOver(globalBoardArray,takenSquaresBoard) != True):
        HumanSequence()
        MachineRegular()
        display_board(globalBoardArray)
    print "game over"


# Human functions

def HumanSequence():
    print "HumanSequence called"
    x = input("Type the x-coordinate of where to put check (0-2)")
    y = input("Type the y-coordinate of where to put check (0-2)")
    while (takenSquaresBoard[x][y] == 1 or x > 2 or y > 2): # if spot is not taken, tell the user to input another location,
        print "Spot is taken, input another location"
        y = input("Type the x-coordinate of where to put check (0-2)")
        x = input("Type the y-coordinate of where to put check (0-2)")
    put_check(x,y)
    if (gameOver(globalBoardArray,takenSquaresBoard)):
        print "game over!"
        return -1


def put_check(userInput1, userInput2):
    globalBoardArray[userInput1][userInput2] = 'X'
    takenSquaresBoard[userInput1][userInput2] = 1
    display_board(globalBoardArray)


# Computer functions

# @Type: Void
# will change these so that they don't make permenat markings on the board: they are hypothetical ones used to calculate the best spot
def HypotheticalVisit(x, y):
    hypotheticalTaken[x][y] = 1
    hypotheticalBoard[x][y] = 'O'

#   @Type: Void 
def markHumanVisit(x, y, board, taken):
    print "human visit called"
    taken[x][y] = 1
    board[x][y] = 'X'

def undoHumanVisit(x, y,board,taken):
    taken[x][y] = 0
    board[x][y] = ' '

def markMachineVisit(x, y, board, taken):
    taken[x][y] = 1
    board[x][y] = 'O'


def GetBoardCopy(board):
    duplicatedBoard = []
    duplicatedBoard = deepcopy(board)  # not sure if need duplicatedBoard = []
    return duplicatedBoard


def MachineRegular():
    print "MachineRegular called"
    if(AttemptWin(globalBoardArray,takenSquaresBoard) == 1):
        print "machine won"
        return
    elif(opponentTwoInRowThreat(globalBoardArray,takenSquaresBoard) is True):
        print "opponentTwoInRowThreat"
        StopOpponentWin(globalBoardArray,takenSquaresBoard)
        return
    elif (globalBoardArray[1][1] == ' '):
        globalBoardArray[1][1] = 'O'
        return
    elif (globalBoardArray[0][0] == ' '):
        globalBoardArray[0][0] = 'O'
        return
    elif (globalBoardArray[2][2] == ' '):
        globalBoardArray[2][2] = 'O'
        return
    elif (globalBoardArray[0][2] == ' '):
        globalBoardArray[0][2] = 'O'
        return
    elif (globalBoardArray[2][0] == ' '):
        globalBoardArray[2][0] = 'O'
        return
    else:
        for x in range(0,3):
            for y in range(0,3):
                if (takenSquaresBoard[x][y] == 0):
                    markMachineVisit(x,y,globalBoardArray,takenSquaresBoard)
                    return
        for x in range(0,3):
            for y in range(0,3):
                if (takenSquaresBoard[x][y] == 0):
                    markMachineVisit(x,y,globalBoardArray,takenSquaresBoard)
                    return

# @Type: Boolean
def opponentTwoInRowThreat(board, taken):
    hypoBoard = GetBoardCopy(board)
    hypoTaken = GetBoardCopy(taken)
    for x in range(0, 3):
        for y in range(0, 3):
            if (hypoTaken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    return True
                else:
                    undoHumanVisit(x, y, hypoBoard, hypoTaken)
    return False


def StopOpponentWin(board,taken):
    hypoBoard = GetBoardCopy(board)
    hypoTaken = GetBoardCopy(taken)
    for x in range(0, 3):
        for y in range(0, 3):
            if (taken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken)):
                    markMachineVisit(x, y, board, taken)
                    return 1
                else:
                    undoHumanVisit(x,y,hypoBoard,hypoTaken)
    for y in range(0, 3):
        for x in range(0, 3):
            if (taken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken)):
                    markMachineVisit(x, y, board, taken)
                    return 1
                else:
                    undoHumanVisit(x,y,hypoBoard,hypoTaken)
    return 0

def AttemptWin(board,taken):
    hypoBoard = GetBoardCopy(board)
    hypoTaken = GetBoardCopy(taken)
    for x in range(0, 3):
        for y in range(0, 3):
            if (taken[x][y] == 0):
                markMachineVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    markMachineVisit(x, y, board, taken)
                    return 1
                else:
                    undoMachineVisit(x,y,hypoBoard,hypoTaken)
    for y in range(0, 3):
        for x in range(0, 3):
            if (taken[x][y] == 0):
                markMachineVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    markMachineVisit(x, y, board, taken)
                    return 1
                else:
                    undoMachineVisit(x,y,hypoBoard,hypoTaken)
    return 0

def undoMachineVisit(x,y,board,taken):
    board[x][y] = ' '
    taken[x][y] = 0

# @Type: boolean
# if there is a winner, terminate; if all spots are taken, terminate
def gameOver(board,taken):
    counter = 0
    #display_board(board)
    for item in enumerate(taken):
        if (item == 1):
            counter = counter + 1
    if (counter == 9):
        print "board is full, game over"
        return True
    if(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):  # first diagonal
        print 2
        return True
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):  # first row
        print 3
        return True
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):  # first column
        print 4
        return True
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):  # second row
        print "5th"
        return True
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):  # third row
        print 6
        return True
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):  # second column
        print 7
        return True
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):  # third column
        print 8
        return True
    elif (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):  # second diagonal
        print 9
        return True  # machine win beginning
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):  # first diagonal
        print "10th"
        return True
    elif (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):  # first row
        print "11th"
        return True
    elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):  # first column
        print 12
        return True
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):  # second row
        print 13
        return True
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):  # third row
        print 14
        return True
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):  # second column
        print 15
        return True
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):  # third column
        print 16
        return True
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):  # second diagonal
        print 17
        return True
    return False


if __name__ == "__main__":
    main()
