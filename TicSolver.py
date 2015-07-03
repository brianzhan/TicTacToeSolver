import operator
from copy import copy, deepcopy


# IMPORTANT NOTE: Human is X, Machine is O

globalBoardArray = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
takenSquaresBoard = [[0,0,0], [0,0,0], [0,0,0]]

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
    while (gameOver(globalBoardArray, takenSquaresBoard) is False):
        HumanSequence() # Technically, there should be a gameOver check, but this is impossible because the machine can't lose
        MachineRegular()
        display_board(globalBoardArray)
        gameOver(globalBoardArray, takenSquaresBoard)  # this is because gameOver NEVER gets called
    print "game over"


def print_welcome_message():
    print "Welcome to the tictactoe player!"

# Human functions

def HumanSequence():
    print "HumanSequence called"
    x = input("Type the x-coordinate of where to put check (0-2)")
    y = input("Type the y-coordinate of where to put check (0-2)")
    while (takenSquaresBoard[x][y] == 1 or x > 2 or y > 2):  # if spot is not taken, tell the user to input another location,
        print "Spot is taken, input another location"
        y = input("Type the x-coordinate of where to put check (0-2)")
        x = input("Type the y-coordinate of where to put check (0-2)")
    put_check(x,y) # includes display board
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
    print "Machine's move:"
    if(AttemptWin(globalBoardArray,takenSquaresBoard) == 1):
        print "machine won"
        return
    elif(opponentTwoInRowThreat(globalBoardArray,takenSquaresBoard) is True):
        StopOpponentWin(globalBoardArray,takenSquaresBoard)
        return
    elif (globalBoardArray[1][1] == ' '):
        globalBoardArray[1][1] = 'O'
        takenSquaresBoard[1][1] = 1
        return
    elif (globalBoardArray[0][0] == ' '):
        globalBoardArray[0][0] = 'O'
        takenSquaresBoard[0][0] = 1
        return
    elif (globalBoardArray[2][2] == ' '):
        globalBoardArray[2][2] = 'O'
        takenSquaresBoard[2][2] = 1
        return
    elif (globalBoardArray[0][2] == ' '):
        globalBoardArray[0][2] = 'O'
        takenSquaresBoard[0][2] = 1
        return
    elif (globalBoardArray[2][0] == ' '):
        globalBoardArray[2][0] = 'O'
        takenSquaresBoard[2][0] = 1
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
    for x in range(0, 3):
        for y in range(0, 3):
            hypoBoard = GetBoardCopy(board)
            hypoTaken = GetBoardCopy(taken)
            if (hypoTaken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    print "game over returned true"
                    return True
    for y in range(0, 3):
        for x in range(0, 3):
            hypoBoard = GetBoardCopy(board)
            hypoTaken = GetBoardCopy(taken)
            if (hypoTaken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    return True
    return False


def StopOpponentWin(board, taken):
    for x in range(0, 3):
        for y in range(0, 3):
            hypoBoard = GetBoardCopy(board)
            hypoTaken = GetBoardCopy(taken)
            print taken
            print x,
            print y,
            if (hypoTaken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    board[x][y] = 'O'
                    display_board(board)
                    return 1
    for y in range(0, 3):
        for x in range(0, 3):
            hypoBoard = GetBoardCopy(board)
            hypoTaken = GetBoardCopy(taken)
            if (hypoTaken[x][y] == 0):
                markHumanVisit(x, y, hypoBoard, hypoTaken)
                if (gameOver(hypoBoard, hypoTaken) is True):
                    board[x][y] = 'O'
                    return 1
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
    for x in range(0,3):
        for y in range(0,3):
            if(taken[x][y] is 1):
                counter = counter + 1
    if (counter is 9):
        return True
    if(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):  # first diagonal
        return True
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):  # first row
        return True
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):  # second row
        return True
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):  # third row
        return True
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):  # first column
        return True
    elif (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):  # second column
        return True
    elif (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):  # third column
        return True
    elif (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):  # second diagonal
        return True  # machine win beginning
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):  # first diagonal
        return True
    elif (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):  # first row
        return True
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):  # second row
        return True
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):  # third row
        return True
    elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):  # first column
        return True
    elif (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):  # second column
        return True
    elif (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):  # third column
        return True
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):  # second diagonal
        return True 
    return False


if __name__ == "__main__":
    main()
