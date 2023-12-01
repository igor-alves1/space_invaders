from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
import random
from ranking import *


def game(screen, difficulty):
    screen.set_title('Kill\'em all!')
    keyboard = screen.get_keyboard()

    player = Animation("nave_spritesheet.png", 2)
    player.set_position((screen.width-player.width)/2, 19/20*(screen.height-player.height))
    player_speed = 150
    player_lives = 3
    invincible_tick = 2
    invincible_timer = 2

    bullet_speed = 400
    bullets_list = []
    bullet_cooldown = 1
    bullet_timer = 0

    col_inimigos = 7
    lin_inimigos = 4
    inimigos = [[], [], [], []]
    inimigo_speed = 100
    for i in range(lin_inimigos):
        for j in range(col_inimigos):
            new_sprite = Sprite("invader.png")
            new_sprite.set_position(new_sprite.width+j*(3*new_sprite.width/2), new_sprite.height+i*(3*new_sprite.height/2))
            inimigos[i].append(new_sprite)
    tiro_inimigo_tick = 2.5/difficulty
    inimigo_timer = 0
    randomx, randomy = 0, 0
    enemy_bullets = []
    
    score = 0
    fps_timer = 0
    frame_rate = 0
    fps = 0

    while True:
        tela_timer = screen.delta_time()
        bullet_timer += tela_timer
        inimigo_timer += tela_timer
        fps += 1
        fps_timer += tela_timer
        if fps_timer >= 1:
        	frame_rate = fps
        	fps = 0
        	fps_timer = 0
        

        #desenha o background, o player e o FPS
        screen.set_background_color((8,24,32))
        player.draw()
        screen.draw_text(f"{player_lives}", x=player.x, y=player.y, color=[0,255,0])
        screen.draw_text(f"{frame_rate}", x=10, y=10, color=[0,255,0])
        screen.draw_text(text=str(score), x=(screen.width/2), y=10, color=[0,255,0])
        
        if keyboard.key_pressed("right"):
        	player.x += player_speed*tela_timer
        elif keyboard.key_pressed("left"):
        	player.x -= player_speed*tela_timer

        #move e desenha a bala
        for item in bullets_list:
            item.draw()
            item.move_y((-bullet_speed)*tela_timer)
        for item in enemy_bullets:
        	item.draw()
        	item.move_y(bullet_speed*tela_timer)

        #move os inimigos
        for i in range(len(inimigos)):
            for j in range(len(inimigos[i])):
                inimigos[i][j].move_x(inimigo_speed*tela_timer)
                inimigos[i][j].draw()

        if inimigos[0][-1].x >= screen.width-(inimigos[0][0].width/2):
            inimigo_speed *= -1
            for i in range(len(inimigos)):
                for j in range(len(inimigos[i])):
                    inimigos[i][j].x -= 5
                    inimigos[i][j].y += 10
        elif inimigos[0][0].x <= inimigos[0][0].width/2:
            inimigo_speed *= -1
            for i in range(len(inimigos)):
                for j in range(len(inimigos[i])):
                    inimigos[i][j].x += 5
                    inimigos[i][j].y += 10

        if inimigos[-1][0].y >= screen.height - 3*player.height or player_lives==0:
            break
        
        #comportamento dos tiros dos inimigos
        if inimigo_timer >= tiro_inimigo_tick:
        	inimigo_timer = 0
        	randomx = random.randint(0, len(inimigos)-1)
        	randomy = random.randint(0, len(inimigos[randomx])-1)
        	new_bullet = Sprite("bullet.png")
        	new_bullet.set_position(inimigos[randomx][randomy].x, inimigos[randomx][randomy].y)
        	enemy_bullets.append(new_bullet)

        #comportamento das balas
        if len(bullets_list):
            if bullets_list[0].y < 0:
                bullets_list.pop(0)
                
            for bullet in bullets_list:
                if bullet.y <= (inimigos[-1][0].y + inimigos[-1][0].height):
                    for lin in inimigos:
                        if bullet.y >= lin[0].y:
                            for enemy in lin:
                                if bullet.collided(enemy):
                                    lin.remove(enemy)
                                    if len(lin) == 0:
                                        inimigos.remove(lin)
                                    bullets_list.remove(bullet)
                                    score += 100
        if len(enemy_bullets):
        	if enemy_bullets[0].y >= screen.height:
        		enemy_bullets.pop(0)
        	elif player.collided(enemy_bullets[0]) and invincible_timer >= invincible_tick:
        		player_lives -= 1
        		enemy_bullets.pop(0)
        		player.set_curr_frame(1)
        		invincible_timer = 0
        
        if invincible_timer < invincible_tick and player.get_curr_frame():
        	invincible_timer += tela_timer
        elif invincible_timer > invincible_tick and player.get_curr_frame():
        	player.set_curr_frame(0)
        	

        if keyboard.key_pressed("SPACE") and bullet_cooldown < bullet_timer:
            new_bullet = Sprite("bullet.png")
            new_bullet.set_position(player.x+(player.width-new_bullet.width)/2, player.y)
            bullets_list.append(new_bullet)
            bullet_timer = 0

        if len(inimigos) == 0:
        	screen.delay(250)
        	difficulty += 0.5
        	tiro_inimigo_tick = 2.5/difficulty
        	inimigos = [[], [], [], []]
        	for i in range(lin_inimigos):
        		for j in range(col_inimigos):
        			new_sprite = Sprite("invader.png")
        			new_sprite.set_position(new_sprite.width+j*(3*new_sprite.width/2), new_sprite.height+i*(3*new_sprite.height/2))
        			inimigos[i].append(new_sprite)
        
        if player_lives <= 0:
        	ranking(screen, score)
        	break
        
        if keyboard.key_pressed('ESC'):
            break

        screen.update()
