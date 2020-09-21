##########################################
####  THIS TIC-TAC-TOE IS NOT COMPETETIVE
##########################################
#imports:
import os
import random

#clear window
def clear():
    os.system('cls')

#num_list for console
num_list = [1,2,3,4,5,6,7,8,9]

#the default console:
grid_index = [str(w) for w in num_list]
def xo_layout(grid):
    ''' This function defines the layout of tic_tac_toe grid'''
    grid_lines = ['-']
    print(' | '.join(grid[0:3]))
    print('  '.join(grid_lines[0]*4))
    print(' | '.join(grid[3:6]))
    print('  '.join(grid_lines[0]*4))
    print(' | '.join(grid[6:9]))

#'o' input by computer
def comp_input(grid_2, user_input_index, lst):
    '''Automates computer inputs'''
    lst.remove(int(grid_2[user_intial_input.x_holder-1]))
    x_random = random.choice(lst)
    grid_2[x_random-1] = 'O'
    lst.remove(x_random)
    #print (x_random) ##

#function for intiating user input
def user_intial_input(grid_1, grid_3):
    play = True
    while play:
        print('\nWhere would you like to place "X": ')
        user_intial_input.x_holder = int(input())
        comp_input(grid_index, user_intial_input, num_list)
        grid_1[user_intial_input.x_holder-1] = 'X'
        clear()
        #if "X, X, X" is continuous in a grid the player wins
        for d in range(0,8):
            if grid_1[d:d+3] == ['X', 'X', 'X']:
                print("WELL PLAYED\n")
                xo_layout(grid_1)
                play = False
        xo_layout(grid_1)
        if len(grid_3) == 1:
            play = False
    else:
        clear()
        print('WELL PLAYED\n')
        grid_1[grid_3[0]-1] = "X"
        return xo_layout(grid_1)

#update console
xo_layout(grid_index)
user_intial_input(grid_index, num_list)
#comp_input(grid_index, user_intial_input, num_list)
#print(num_list) #### for checking the updated num_list
