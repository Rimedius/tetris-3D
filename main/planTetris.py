import numpy as np
from main import tetrislib

# Game setup
# _________________________________________________________________ #
LEVEL = 1
FIELD_SIZE = 5
PLAYER_BAR_CHOICE = {
    "a": 0,
    "s": 1,
    "d": 2
}

# Game "state"
# _________________________________________________________________ #
gameboard = np.zeros((FIELD_SIZE, FIELD_SIZE))
blocks = {
    0: [[1, 0], [0, 0]],
    1: [[1, 1], [0, 0]]
}

GAME_RUN = True

# Hello screen
# _________________________________________________________________ #

print('Welcome to Tetris 3D')
print('Copyright Masa 2020')

while GAME_RUN:
    print(gameboard)

    '''
    load bar:
     - choose blocks -> from blocks library
     - generate blocks levels
    '''
    bar = tetrislib.make_bar(blocks)

    # Until player doesn't choice correct option
    selected_block = None
    while selected_block is None:

        print('__[a]______[s]______[d]___')
        print(bar[0][0], bar[1][0], bar[2][0])
        print(bar[0][1], bar[1][1], bar[2][1])
        print('____________________')

        # choose block (1-3)

        choice = input('choose the block  ')
        if choice in PLAYER_BAR_CHOICE:
            selected_block = bar[PLAYER_BAR_CHOICE[choice]]
        else:
            print("Wrong option")

    # Select roration
    continue_select = True
    while continue_select:
        # rotate blok (n-times)
        rotation = input(f'rotation\n [a] < {selected_block} > [d]  (or [s] for end rotation)\n')
        if rotation == "a":
            selected_block = np.rot90(selected_block, 1)
        elif rotation == "d":
            selected_block = np.rot90(selected_block, 1, (1, 0))
        elif rotation == "s":
            continue_select = False

        print(selected_block)

    # Get real bounding box of selected block
    # TODO: how about situation [5, 1], [1, 5] ??
    width_block, height_block = max(np.nonzero(selected_block), key=lambda x: x[1])

    # Select position on gameboard
    continue_select = True
    while continue_select:

        print("Gameboard --------------------------")
        print(gameboard)
        print("Selected block ---------------------")
        print(selected_block)

        index_x = int(input('choose the number of a row   '))
        index_y = int(input('choose the number of a column   '))
        print(f'you choose: {index_x} - {index_y}')

        # Check if player select valid index of
        if (index_x >= 0 and (index_x+width_block) < gameboard.shape[0]) and \
            (index_y >= 0 and (index_y+height_block) < gameboard.shape[1]):

            continue_select = False
        else :
            print(f"Cannot fit block!")

    # Place block into gameboard
    # TODO: change the logic -> this couldn't work
    gameboard[index_x:index_x + selected_block.shape[0], index_y:index_y + selected_block.shape[1]] += selected_block

    '''gamelogic actions
    take place -> check place y/n
    n ->add new place
    y: refresh fild
    chek nozero raws and columns -> y/n
    
    '''

    '''
    Check end of game
    '''

'''
Print score and say goodbye to player 
'''
