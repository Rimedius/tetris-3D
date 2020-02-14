import random
import numpy as np
import copy
import tetrislib


print('START YOU GAME' )
print('____________________')
level = 1
fild_size = 5
fild = np.zeros((fild_size, fild_size))
bloks = {0:[[1,0],[0,0]], 1:[[1,1],[0,0]]}

'while is not game over'

'load fild'
print(fild)

'''
load bar:
 - choose bloks -> ftom bloks library
 - generate bloks lavels
'''
bar = tetrislib.make_bar(bloks) 
print('__a______s______d___')
print(bar[0][0],bar[1][0],bar[2][0])
print(bar[0][1],bar[1][1],bar[2][1])
print('____________________')




'start game'

''' player actions
choose blok (1-3)
rotate blok (n-times)
set blok -> add place
'''

'''gamelogic actions
take place -> check place y/n
n ->add new place
y: refresh fild
chek nozero raws and columns -> y/n



'''
