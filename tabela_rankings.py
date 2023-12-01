from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.animation import *

def exibir(screen):
    mouse = screen.get_mouse()
    keyboard = screen.get_keyboard()
    my_file = open("ranking.txt", 'r')
    rankings_ordenados = []
    for line in my_file:
    	ranking = line
    	lista = ranking.split()
    	nome = lista[0]
    	score = int(lista[1])
    	tupla = (nome, score)
    	rankings_ordenados.append(tupla)
    novos_rankings = sorted(rankings_ordenados, key=lambda ranking: ranking[1])
    novos_rankings.reverse()
    my_file.close()
        
    while True:
        screen.set_background_color((8,24,32))
        screen.draw_text("RANKING: ", x=screen.width/10, y=screen.height/10, color=(0,255,0),size=24, bold=True)
        if len(novos_rankings)>=5:
        	for i in range(5):
        		screen.draw_text(f"{novos_rankings[i][0]}..............{novos_rankings[i][1]}", x=screen.width/10, y=(i+2)*screen.height/10, color=(0,255,0),size=18)
        else:
        	for i in range(len(novos_rankings)):
        		screen.draw_text(f"{novos_rankings[i][0]}..............{novos_rankings[i][1]}", x=screen.width/10, y=(i+2)*screen.height/10, color=(0,255,0),size=18)
        if keyboard.key_pressed('esc'):
        	return 1
	
        screen.update()
