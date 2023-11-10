from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *



def game(screen, difficulty):
    screen.set_title('Igor Rodrigues Alves')
    keyboard = screen.get_keyboard()

    player = Sprite("spaceship.png")
    player.set_position((screen.width-player.width)/2, 19/20*(screen.height-player.height))
    player_speed = 150

    bullet_speed = 300
    bullets_list = []
    bullet_cooldown = 1
    bullet_timer = 0

    col_inimigos = 6
    lin_inimigos = 4
    inimigos = [[], [], [], []]
    inimigo_speed = 100
    
    for i in range(lin_inimigos):
        for j in range(col_inimigos):
            new_sprite = Sprite("invader.png")
            new_sprite.set_position(new_sprite.width+j*(3*new_sprite.width/2), new_sprite.height+i*(3*new_sprite.height/2))
            inimigos[i].append(new_sprite)

    while True:
        tela_timer = screen.delta_time()
        bullet_timer += tela_timer
        
        screen.set_background_color((8,24,32))
        player.draw()
        player.move_key_x(player_speed * tela_timer)

        for item in bullets_list:
            item.draw()
            item.move_y((-bullet_speed)*tela_timer)

        for i in range(lin_inimigos):
            for j in range(col_inimigos):
                inimigos[i][j].move_x(inimigo_speed*tela_timer)
                inimigos[i][j].draw()

        if inimigos[0][-1].x >= screen.width-(inimigos[0][0].width/2) or inimigos[0][0].x <= inimigos[0][0].width/2:
            inimigo_speed *= -1
            for i in range(lin_inimigos):
                for j in range(col_inimigos):
                    inimigos[i][j].y += 10

        if inimigos[-1][0].y >= screen.height - 3*player.height:
            break

        if len(bullets_list) and bullets_list[0].y > screen.height:
            bullets_list.pop(0)

        if keyboard.key_pressed("SPACE") and bullet_cooldown < bullet_timer:
            new_bullet = Sprite("bullet.png")
            new_bullet.set_position(player.x+(player.width-new_bullet.width)/2, player.y)
            bullets_list.append(new_bullet)
            bullet_timer = 0

        if keyboard.key_pressed('ESC'):
            break

        screen.update()
