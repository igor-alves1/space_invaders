from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.animation import *

def menu(screen):
    mouse = screen.get_mouse()
    keyboard = screen.get_keyboard()
    
    play_button = Animation("spritesheet_play.png", 3, loop=True)
    play_button.set_total_duration(1000) 
    play_button.set_position((screen.width-play_button.width)/2, (screen.height-play_button.height)*(3/8))

    diff_button = Animation("spritesheet_diff.png", 2, loop=True)
    diff_button.set_total_duration(1000)
    diff_button.set_position(play_button.x, (screen.height-play_button.height)*(4/8))

    rank_button = Sprite("rank_button.png")
    rank_button.set_position(diff_button.x, (screen.height-play_button.height)*(5/8))

    quit_button = Animation("spritesheet_sair.png", 2, loop=True)
    quit_button.set_total_duration(1000)
    quit_button.set_position(diff_button.x, (screen.height-play_button.height)*(6/8))
        
    while True:
        screen.set_background_color((8,24,32))
        play_button.update()
        diff_button.update()
        rank_button.draw()

        if mouse.is_over_object(play_button):
            play_button.play()
            play_button.draw()

            if mouse.is_button_pressed(1):
                return 2
        else:
            play_button.stop()
            play_button.draw()

        if mouse.is_over_object(diff_button):
            diff_button.play()
            diff_button.draw()

            if mouse.is_button_pressed(1):
                return 3
        else:
            diff_button.stop()
            diff_button.draw()

        if mouse.is_over_object(rank_button) and mouse.is_button_pressed(1):
            pass

        if mouse.is_over_object(quit_button):
            quit_button.play()
            quit_button.draw()

            if mouse.is_button_pressed(1):
                screen.close()
        else:
            quit_button.stop()
            quit_button.draw()

        screen.update()
