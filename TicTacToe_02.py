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
be able to quit and go again after each cycle
see tournament score
save tournament state
"""

board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board_state(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')  
    
def player_move():
    run = True
    while run:
        move = input('Select a position to put and "X" (1-9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('This space is occupied')
            else:
                print('Please type a number between 1 and 9.')
        except:   
            print('Type a number!')
    
def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
            
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7 ,9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move
    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    

def is_board_full():
    if board.count(' ') > 1:
        return False
    else:
        return True

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def main():
    print("Welcome to Xes and Oes!")
    print_board_state(board)
    
    while not is_board_full():
        if not is_winner(board, 'O'):
            player_move()
            print_board_state(board)
        else:
            print('Sorry, Oes won baby')
            break
        
        if not is_winner(board, 'X'):
            move = computer_move()
            if move == 0:
                print('why is this here')
            else:
                insert_letter('O', move)
                print('Computer placed an "O" in position', move, ':')
                print_board_state(board)
        else:
            print('Good one, eXes won baby')
            break
        
    if is_board_full():
        print('Tie game!')

main()