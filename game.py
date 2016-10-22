from gameoflife_no_loops import Game, Alive, Dead
from itertools import count
from time import sleep
import os

clear = lambda: os.system('clear')

game = Game(10, 20)
game.set(0, 0, Alive)
game.set(1, 0, Alive)
game.set(2, 0, Alive)
game.set(0, 1, Alive)
game.set(1, 2, Alive)

game.set(4, 5, Alive)
game.set(5, 5, Alive)
game.set(6, 5, Alive)

def change_state(i):
    game.change_states()
    print('state %d' % i)
    print(str(game))
    sleep(0.1)
    clear()
    
list(map(change_state, count()))
