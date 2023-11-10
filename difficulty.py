from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *

def diff(screen):
    mouse = screen.get_mouse()

    easy_button = Sprite("easy_button.png")
    easy_button.set_position((screen.width-easy_button.width)/2, (screen.height-easy_button.height)*(3/8))

    medium_button = Sprite("medium_button.png")
    medium_button.set_position(easy_button.x, (screen.height-easy_button.height)*(4/8))

    hard_button = Sprite("hard_button.png")
    hard_button.set_position(easy_button.x, (screen.height-easy_button.height)*(5/8))

    delay = 1
    timer_delay = 0
    
    while True:
        screen.set_background_color((8, 24, 32))

        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

        if mouse.is_over_object(easy_button) and mouse.is_button_pressed(1) and timer_delay > delay:
            return 0.75

        if mouse.is_over_object(medium_button) and mouse.is_button_pressed(1) and timer_delay > delay:
            return 1
        if mouse.is_over_object(hard_button) and mouse.is_button_pressed(1) and timer_delay > delay:
            return 1.5
            
        timer_delay += screen.delta_time()
        screen.update()
