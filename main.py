from menu import *
from game import *
from difficulty import *
from PPlay.window import *
from tabela_rankings import * 

GAME_STATE = 1
GAME_DIFF = 1
GAME_SCREEN = Window(600, 600)

while True:
    if GAME_STATE == 1:
        GAME_STATE = menu(GAME_SCREEN)
    elif GAME_STATE == 2:
        GAME_STATE = 1
        game(GAME_SCREEN, GAME_DIFF)
        GAME_DIFF = 1
    elif GAME_STATE == 3:
        GAME_STATE = 2
        GAME_DIFF = diff(GAME_SCREEN)
    elif GAME_STATE == 4:
    	GAME_STATE = exibir(GAME_SCREEN)
