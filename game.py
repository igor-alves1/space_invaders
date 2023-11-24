from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *


def game(screen, difficulty):
    screen.set_title('Kill\'em all!')
    keyboard = screen.get_keyboard()

    player = Sprite("spaceship.png")
    player.set_position((screen.width-player.width)/2, 19/20*(screen.height-player.height))
    player_speed = 150

    bullet_speed = 300
    bullets_list = []
    bullet_cooldown = 1
    bullet_timer = 0

    col_inimigos = 7
    lin_inimigos = 4
    inimigos = [[], [], [], []]
    inimigo_speed = 100

    score = 0
    victory = False
    
    for i in range(lin_inimigos):
        for j in range(col_inimigos):
            new_sprite = Sprite("invader.png")
            new_sprite.set_position(new_sprite.width+j*(3*new_sprite.width/2), new_sprite.height+i*(3*new_sprite.height/2))
            inimigos[i].append(new_sprite)

    while True:
        tela_timer = screen.delta_time()
        bullet_timer += tela_timer

        #desenha o background, o player e o FPS
        screen.set_background_color((8,24,32))
        player.draw()
        player.move_key_x(player_speed * tela_timer)
        frame_rate = 1/tela_timer
        screen.draw_text(f"{frame_rate:.0f}", x=10, y=10, color=[0,255,0])
        screen.draw_text(text=str(score), x=(screen.width/2), y=10, color=[0,255,0])

        if victory:
            screen.delay(3000)
            break

        #move e desenha a bala
        for item in bullets_list:
            item.draw()
            item.move_y((-bullet_speed)*tela_timer)

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

        if inimigos[-1][0].y >= screen.height - 3*player.height:
            break

        #comportamento das balas
        if len(bullets_list):
            if bullets_list[0].y > screen.height:
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
                    

        if keyboard.key_pressed("SPACE") and bullet_cooldown < bullet_timer:
            new_bullet = Sprite("bullet.png")
            new_bullet.set_position(player.x+(player.width-new_bullet.width)/2, player.y)
            bullets_list.append(new_bullet)
            bullet_timer = 0

        if len(inimigos) == 0:
            victory = True
            screen.draw_text("YOU WIN!!!", size=30, x=270, y=270, color=[0,255,0])

        if keyboard.key_pressed('ESC'):
            break

        screen.update()
