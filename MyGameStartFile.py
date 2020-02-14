import random
'import mytetris'
import numpy as np
import copy

number_variants_blocks=2
number_blocks=3
fild_size=5
level=1

bloks = {0:[[1,0],[0,0]], 1:[[1,1],[0,0]]}
fild = np.zeros((fild_size, fild_size))

# Hello GitHUb

print('START YOU GAME' )
abc = np.array(['a','b','c','d','e'])

# fild[0,:] = abc
# fild = np.insert(fild, 0, abc, axis=1)
# fild = np.stack((abc, fild))
print(fild)

bar = [0, 0, 0]
for i in range(3):
    bar[i] = bloks[np.random.randint(2)]
print('___a_______s_______d____')
print(bar[0][0],bar[1][0],bar[2][0])
print(bar[0][1],bar[1][1],bar[2][1])

my_blok = input('choose the block  ')
if my_blok in ['a', 's', 'd']:
    if my_blok == 'a': my_blok=0
    elif my_blok == 's': my_blok=1
    else: my_blok=2
    blok = bar[my_blok]
    print(f'you choose:  {my_blok} \n {blok}')
    rotation = input(f'rotation\n a < {blok} > d \n')
    if rotation == 'a':
        myblok = copy.deepcopy(blok)
        blok[0][0] = myblok[0][1]
        blok[0][1] = myblok[1][1]
        blok[1][1] = myblok[1][0]
        blok[1][0] = myblok[0][0] 
        print(blok[0],'\n',blok[1])
    elif rotation == 'd':
        print(blok)
        myblok = copy.deepcopy(blok)
        print(myblok)
        blok[0][0] = myblok[1][0]
        blok[1][0] = myblok[1][1]
        blok[1][1] = myblok[0][1]
        blok[0][1] = myblok[0][0] 
        print(' ',blok[0],'\n',blok[1])
    else:
        index_x = int(input('choose the number of a row   '))
        index_y = int(input('choose the number of a column   '))
        print(f'you choose: {index_x} - {index_y}')

        for i in range(2):
            fild[index_y][index_x+i] = blok[i]

        print(fild)
else:
    print('you are wrong. Bay-bay!')




