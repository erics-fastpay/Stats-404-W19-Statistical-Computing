import random

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def random_result(): 
    #random shuffle the input order of these 9 positions, use the new order to play the game
    items = ['top-L', 'top-M', 'top-R',
            'mid-L', 'mid-M', 'mid-R',
            'low-L', 'low-M', 'low-R']
    random.shuffle(items)
    return(items)

def check_win(theBoard):
    if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R']!=' ' or\
        theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R']!=' ' or\
        theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R']!=' ' or\
        theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L']!=' ' or\
        theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M']!=' ' or\
        theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R']!=' ' or\
        theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R']!=' ' or\
        theBoard['low-L'] == theBoard['mid-M'] == theBoard['top-R']!=' ':
        return(1)
    else:
        return(0)

def play():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print('game start, player X first, player O second')
    result = random_result()
    # print(result)
    for i in range(9):
        if i % 2 == 0: #odd number of play, belongs to player X
            theBoard[result[i]] = 'X'
            printBoard(theBoard)
            if check_win(theBoard) ==1:
                print('player X won! game stop')
                break
        if i % 2 == 1: #even number of play, belongs to player O
            theBoard[result[i]] = 'O'
            printBoard(theBoard)
            if check_win(theBoard) ==1:
                print('player O won! game stop')
                break
        if i == 8 and check_win(theBoard) == 0: #check tie
            print('TIE, no winner this time.')
        else:
            print('next player')