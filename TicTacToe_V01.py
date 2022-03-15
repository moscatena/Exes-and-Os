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
see tournament score
save tournament state
"""
import random

def greeting():
    global choice_1
    choice_1 = input("\nWelcome to TicTacToe, or Exes and Oes, or Knots and Crosses. Are you playing against the Computer (type 'c') or against a Friend (type 'f')?\n")
    while choice_1 not in ['c', 'f']:
        choice_1 = input("Not a valid command. Try again. Are you playing against the Computer (type 'c') or against a Friend (type 'f')?\n")       
        if choice_1 in ['c', 'f']:
            break
        

def choose_x_or_o():
    global choice_2
    if choice_1 == 'f':
        print("So you're playing against a buddy.\nThe first player will be 'X', the second 'O'. Have fun!")
        choice_2 = 'buddy'
        
    if choice_1 == 'c':
        choice_2 = input("So you're playing against the computer.\nWould you like to play first (type 'f') or second(type 's')?\n")
        while choice_2 not in ['f', 's']:
            choice_2 = input("Not a valid command. Try again.\n Are you going first ('f') or second ('s')?\n")
            if choice_2 in ['f', 's']:
                break
        
def current_board():
    a = ("\n     |     |     ")
    b = ("\n     |     |     ")
    c = ("\n_____|_____|_____")
    d = ("\n     |     |     ")
    e = ("\n     |     |     ")
    f = ("\n_____|_____|_____")
    g = ("\n     |     |     ")
    h = ("\n     |     |     ")
    i = ("\n     |     |     ")
    
    for x in player_1_moves:
        if x == 'A1':
            b = b[0:3] + "X" + b[4:]
        if x == 'A2':
            b = b[0:9] + "X" + b[10:]
        if x == 'A3':
            b = b[0:15] + "X" + b[16:]
        if x == 'B1':
            e = e[0:3] + "X" + e[4:]
        if x == 'B2':
            e = e[0:9] + "X" + e[10:]
        if x == 'B3':
            e = e[0:15] + "X" + e[16:]
        if x == 'C1':
            h = h[0:3] + "X" + h[4:]
        if x == 'C2':
            h = h[0:9] + "X" + h[10:]
        if x == 'C3':
            h = h[0:15] + "X" + h[16:]
            
    for o in player_2_moves:
        if o == 'A1':
            b = b[0:3] + "O" + b[4:]
        if o == 'A2':
            b = b[0:9] + "O" + b[10:]
        if o == 'A3':
            b = b[0:15] + "O" + b[16:]
        if o == 'B1':
            e = e[0:3] + "O" + e[4:]
        if o == 'B2':
            e = e[0:9] + "O" + e[10:]
        if o == 'B3':
            e = e[0:15] + "O" + e[16:]
        if o == 'C1':
            h = h[0:3] + "O" + h[4:]
        if o == 'C2':
            h = h[0:9] + "O" + h[10:]
        if o == 'C3':
            h = h[0:15] + "O" + h[16:]
            
    for x in player_moves_x:
        if x == 'A1':
            b = b[0:3] + "X" + b[4:]
        if x == 'A2':
            b = b[0:9] + "X" + b[10:]
        if x == 'A3':
            b = b[0:15] + "X" + b[16:]
        if x == 'B1':
            e = e[0:3] + "X" + e[4:]
        if x == 'B2':
            e = e[0:9] + "X" + e[10:]
        if x == 'B3':
            e = e[0:15] + "X" + e[16:]
        if x == 'C1':
            h = h[0:3] + "X" + h[4:]
        if x == 'C2':
            h = h[0:9] + "X" + h[10:]
        if x == 'C3':
            h = h[0:15] + "X" + h[16:]
            
    for o in player_moves_o:
        if o == 'A1':
            b = b[0:3] + "O" + b[4:]
        if o == 'A2':
            b = b[0:9] + "O" + b[10:]
        if o == 'A3':
            b = b[0:15] + "O" + b[16:]
        if o == 'B1':
            e = e[0:3] + "O" + e[4:]
        if o == 'B2':
            e = e[0:9] + "O" + e[10:]
        if o == 'B3':
            e = e[0:15] + "O" + e[16:]
        if o == 'C1':
            h = h[0:3] + "O" + h[4:]
        if o == 'C2':
            h = h[0:9] + "O" + h[10:]
        if o == 'C3':
            h = h[0:15] + "O" + h[16:]
            
    for x in computer_moves_x:
        if x == 'A1':
            b = b[0:3] + "X" + b[4:]
        if x == 'A2':
            b = b[0:9] + "X" + b[10:]
        if x == 'A3':
            b = b[0:15] + "X" + b[16:]
        if x == 'B1':
            e = e[0:3] + "X" + e[4:]
        if x == 'B2':
            e = e[0:9] + "X" + e[10:]
        if x == 'B3':
            e = e[0:15] + "X" + e[16:]
        if x == 'C1':
            h = h[0:3] + "X" + h[4:]
        if x == 'C2':
            h = h[0:9] + "X" + h[10:]
        if x == 'C3':
            h = h[0:15] + "X" + h[16:]
            
    for o in computer_moves_o:
        if o == 'A1':
            b = b[0:3] + "O" + b[4:]
        if o == 'A2':
            b = b[0:9] + "O" + b[10:]
        if o == 'A3':
            b = b[0:15] + "O" + b[16:]
        if o == 'B1':
            e = e[0:3] + "O" + e[4:]
        if o == 'B2':
            e = e[0:9] + "O" + e[10:]
        if o == 'B3':
            e = e[0:15] + "O" + e[16:]
        if o == 'C1':
            h = h[0:3] + "O" + h[4:]
        if o == 'C2':
            h = h[0:9] + "O" + h[10:]
        if o == 'C3':
            h = h[0:15] + "O" + h[16:]
        
    print(a, b, c, d, e, f, g, h, i)

def print_board_state():
    print("\nCurrent boardstate: ")
    current_board()
    
def player_move_x():
    global p_move
    global count
    choices_str = ""
    for choice in choices:
        choices_str += choice + ", "
    choices_str = choices_str[0:-2]
    p_move = input("Where are you marking 'X'?\nChoices are {}.\n".format(choices_str))
    while p_move not in choices:
        p_move = input("Not a valid command. Try again\nYour choices are {}.\n".format(choices_str))
    choices.remove(p_move)
    count += 1
    player_moves_x.append(p_move)
    
def player_move_o():
    global p_move
    global count
    choices_str = ""
    for choice in choices:
        choices_str += choice + ", "
    choices_str = choices_str[0:-2]
    p_move = input("Where are you marking 'O'?\nChoices are {}.\n".format(choices_str))
    while p_move not in choices:
        p_move = input("Not a valid command. Try again\nYour choices are {}.\n".format(choices_str))
    choices.remove(p_move)
    count += 1
    player_moves_o.append(p_move)
    
def computer_move_x():
    global computer_move
    global count
    computer_move = random.choice(choices)
    choices.remove(computer_move)
    count += 1
    computer_moves_x.append(computer_move)
    

def computer_move_o():
    global computer_move
    global count
    computer_move = random.choice(choices)
    choices.remove(computer_move)
    count += 1
    computer_moves_o.append(computer_move)


def player_1_move():
    global p1_move
    global count
    choices_str = ""
    for choice in choices:
        choices_str += choice + ", "
    choices_str = choices_str[0:-2]
    p1_move = input("Where are you marking 'X'?\nChoices are {}.\n".format(choices_str))
    while p1_move not in choices:
        p1_move = input("Not a valid command. Try again\nYour choices are {}.\n".format(choices_str))
    choices.remove(p1_move)
    count += 1
    player_1_moves.append(p1_move)
    

def player_2_move():
    global p2_move
    global count
    choices_str = ""
    for choice in choices:
        choices_str += choice + ", "
    choices_str = choices_str[0:-2]
    p2_move = input("Where are you marking 'O'?\nChoices are {}.\n".format(choices_str))
    while p2_move not in choices:
        p2_move = input("Not a valid command. Try again\nYour choices are {}.\n".format(choices_str))
    choices.remove(p2_move)
    count += 1
    player_2_moves.append(p2_move)

def is_board_full():
    if count == 9:
        print("The game was a tie!")
        exit()

def is_winner():
    win_1 = ['A1', 'B1', 'C1']
    win_2 = ['A2', 'B2', 'C2']
    win_3 = ['A3', 'B3', 'C3']
    win_4 = ['A1', 'A2', 'A3']
    win_5 = ['B1', 'B2', 'B3']
    win_6 = ['C1', 'C2', 'C3']
    win_7 = ['A1', 'B2', 'C3']
    win_8 = ['C1', 'B2', 'A3']
    win_list = [win_1, win_2, win_3, win_4, win_5, win_6, win_7, win_8]
    
    for win in win_list:
        if win[0] in player_1_moves and win[1] in player_1_moves and win[2] in player_1_moves:
            print("\nCongratulations! 'X' won!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
    for win in win_list:
        if win[0] in player_2_moves and win[1] in player_2_moves and win[2] in player_2_moves:
            print("\nCongratulations! 'O' won!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
    for win in win_list:
        if win[0] in player_moves_x and win[1] in player_moves_x and win[2] in player_moves_x:
            print("\nCongratulations! You beat the machine!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
    for win in win_list:
        if win[0] in computer_moves_x and win[1] in computer_moves_x and win[2] in computer_moves_x:
            print("\nDamn! The machine beat you!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
    for win in win_list:
        if win[0] in player_moves_o and win[1] in player_moves_o and win[2] in player_moves_o:
            print("\nCongratulations! You beat the machine!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
    for win in win_list:
        if win[0] in computer_moves_o and win[1] in computer_moves_o and win[2] in computer_moves_o:
            print("\nDamn! The machine beat you!\nWinnig slots were: {0}, {1}, {2}!".format(win[0], win[1], win[2]))
            exit()
            
            

def main():
    global choices
    global count
    global player_moves_x
    global computer_moves_x
    global player_moves_o
    global computer_moves_o
    global player_1_moves
    global player_2_moves
    global winner
    winner = False
    choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    count = 0
    player_moves_x = []
    computer_moves_x = []
    player_moves_o = []
    computer_moves_o = []
    player_1_moves = []
    player_2_moves = []
    greeting()
    choose_x_or_o()
    if choice_2 == 'buddy':
        while winner == False:
            print_board_state()
            player_1_move()
            is_winner()
            is_board_full()
            print_board_state()
            player_2_move()
            is_winner()
            is_board_full()
    elif choice_2 == 'f':
        while winner == False:
            print_board_state()
            player_move_x()
            is_winner()
            is_board_full()
            computer_move_o()
            is_winner()
            is_board_full()
    else:
        while winner == False:
            computer_move_x()
            print_board_state()
            is_winner()
            is_board_full()
            player_move_o()
            print_board_state()
            is_winner()
            is_board_full()
        

        


main()