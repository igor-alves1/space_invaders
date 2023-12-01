from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *

def ranking(screen, score):
    my_file = open("ranking.txt", 'a')
    while True:
        screen.set_background_color((8, 24, 32))
        screen.draw_text(f"Congratulations! You scored {score}!\nTell us your name(no terminal)", x=screen.width/4, y=screen.height/2, color=[0,255,0])
        screen.update()
        nome = input("Digite seu nome: ")
        my_file.write(f"{nome} {score}\n")
        my_file.close()
        break
