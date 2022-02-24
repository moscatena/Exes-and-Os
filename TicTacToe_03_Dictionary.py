# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:15:05 2021

@author: Scatena
"""

"""
See Board at all times - ok
Choose next move - ok
See moves made by all - ok
see who won and why - ok
be able to quit and go again after each cycle - ok
see tournament score - ok
computer makes nearly optimal moves
"""

def display_board(theBoard):    
    print('  ', theBoard['7'], '  |','  ' ,theBoard['8'], '  |', '  ',theBoard['9'])
    print('-------+--------+--------')
    print('  ', theBoard['4'], '  |','  ' ,theBoard['5'], '  |', '  ',theBoard['6'])
    print('-------+--------+--------')
    print('  ', theBoard['1'], '  |','  ' ,theBoard['2'], '  |', '  ',theBoard['3'], '\n')
        
def instruction(node):
    print("press the numbers to place your {} in position\n".format(node))    
    print('  ', '7', '  |','  ' ,'8', '  |', '  ','9')
    print('-------+--------+--------')
    print('  ', '4', '  |','  ' ,'5', '  |', '  ','6')
    print('-------+--------+--------')
    print('  ', '1', '  |','  ' ,'2', '  |', '  ','3', '\n')
    print('=========================\n')
         
def is_winner(theBoard, node, x_score=0, o_score=0, comp_test=False):
    # checks all winning scenarios
    # comp_test runs only inside computer_play def
    check = 0
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' :
        check = '7, 8, 9'
    elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
        check = '7, 4, 1'
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
        check = '7, 5, 3'
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
        check = '4, 5, 6'
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        check = '1, 2, 3'
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        check = '1, 5, 9'
    elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
        check = '9, 6, 3'
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        check = '2, 5, 8'
    if comp_test == True:
        if check == 0:
            return False
        return True
    if check == 0:
        return check, x_score, o_score

    print('=========================\n')
    display_board(theBoard)
    print('{} won!\nwinning places were {}'.format(node, check))
    if node == 'X':
        x_score += 1
    else:
        o_score += 1
    return check, x_score, o_score
      
def is_space(theBoard, win):
    for i in theBoard.values():
        if i == ' ':
            return True
    if win == 0:
        display_board(theBoard)
        print('you ran out of space')
        print('=========================\n')
    return False

def is_empty(theBoard):
    if theBoard == {'7': ' ', '8': ' ', '9': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '1': ' ', '2': ' ', '3': ' '}:
        return True
    return False
            
def computer_or_friend():
    choice = input('Would you like to play against a friend or the computer? f/c\n')
    if choice == 'f':
        return True
    if choice == 'c':
        return False
    else:
        print('We\'re gonna try this again...')
        return computer_or_friend()
    
def player_first():
    first = input('are you playing first? y/n\n')
    if first == 'y':
        return True
    if first == 'n':
        return False
    else:
        print('We\'re gonna try this again...')
        player_first()

def change_node(node):
    if node == 'X':
        node = 'O'
    else:
        node = 'X'
    return node

def play(theBoard, node):
    valid_input = ['1','2','3','4','5','6','7','8','9']
    turn = input('it is {} turn to play\n'.format(node))
    # asks for a play until valid input
    while turn not in valid_input or theBoard[turn] != ' ':
        print('that is not a valid command. Place your', node, 'somewhere valid')
        turn = input('')
        if turn in valid_input and theBoard[turn] == ' ':
            break
    theBoard[turn] = node
    return node

def computer_play(theBoard, node):
    import random
    #checks if comp can win, then if player can win
    possible_moves = []
    for k in theBoard.keys():
        if theBoard[k] == ' ':
            possible_moves.append(k)
    for letter in [node, change_node(node)]:
        for i in possible_moves:
            boardCopy = theBoard.copy()
            boardCopy[i] = letter
            if is_winner(boardCopy, node, comp_test=True):
                theBoard[i] = node
                return theBoard
    
    # selects the middle if it's free
    if theBoard['5'] == ' ':
        theBoard['5'] = node
    
    # selects a random empty corner
    elif theBoard['1'] == ' ' or theBoard['3'] == ' ' or theBoard['7'] == ' ' or theBoard['9'] == ' ':
        options = [1, 3, 7, 9]
        while options:
            random_idx = random.randint(0, len(options) - 1)
            random_corner = options[random_idx]
            if theBoard[str(random_corner)] != ' ':
                options.remove(random_corner)
            else:
                theBoard[str(random_corner)] = node
                break
    else:
    # selects a random empty edge
        options = [2, 4, 6, 8]
        while options:
            random_idx = random.randint(0, len(options) - 1)
            random_corner = options[random_idx]
            if theBoard[str(random_corner)] != ' ':
                options.remove(random_corner)
            else:
                theBoard[str(random_corner)] = node
                break
    return theBoard

def replay(x_score, o_score, theBoard):
    cont = input('would you like to play again? y/n\n')
    while cont not in ['y', 'n']:
        cont = input('a simple yes or no will do. y/n\n')
    if cont == 'n':
        print('=========================\n')
        print('alright then.\n\'X\' scored {} and \'O\' scored {}.\nSee you next time!'.format('once' if x_score == 1 else str(x_score) + ' times', 'once' if o_score == 1 else str(o_score) + ' times'))
        return cont
    else:
        print('current score are {} to \'X\' and {} to \'O\''.format(x_score, o_score))
        print('=========================\n')
        for k, v in theBoard.items():
            if v != ' ':
                theBoard[k] = ' '
        return theBoard
        

        
def main():
    theBoard = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}
    node = 'O'
    x_score = 0
    o_score = 0
    keep_going = True
    friend = computer_or_friend()
    
    if friend == False:
        pf = player_first()
        
    while keep_going:
        if not friend:
            if pf == False and is_empty(theBoard):
                node = change_node(node)
                computer_play(theBoard, node)
                 
        node = change_node(node)
        instruction(node)
        display_board(theBoard)
        play(theBoard, node)
        win, x_score, o_score = is_winner(theBoard, node, x_score, o_score)
        space = is_space(theBoard, win)
        if win != 0 or not space:
            if replay(x_score, o_score, theBoard) =='n':
                keep_going = False
                break
            node = 'O'
            
        if friend == False and not is_empty(theBoard):
            node = change_node(node)
            computer_play(theBoard, node)
            win, x_score, o_score = is_winner(theBoard, node, x_score, o_score)
            space = is_space(theBoard, win)
            if win != 0 or not space:
                if replay(x_score, o_score, theBoard) =='n':
                    keep_going = False
                    break
                node = 'O'
                
    
if __name__ == '__main__':
    main()