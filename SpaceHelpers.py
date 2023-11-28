import random

import arcade

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800

def make_rocks():
    rock_list = arcade.SpriteList()
    possible_rocks = [
        ":resources:images/space_shooter/meteorGrey_med1.png",
        ":resources:images/space_shooter/meteorGrey_med2.png",
        ":resources:images/space_shooter/meteorGrey_big4.png",
        ":resources:images/space_shooter/meteorGrey_big2.png"
    ]
    for rock_number in range(10):
        file_name = random.choice(possible_rocks)
        rock  = arcade.Sprite(file_name)
        rock.center_x = random.randint(150, WINDOW_WIDTH)
        rock.center_y = random.randint(0, WINDOW_HEIGHT)
        rock_list.append(rock)
    return rock_list