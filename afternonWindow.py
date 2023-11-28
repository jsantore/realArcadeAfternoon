import random

import arcade

WINDOW_WIDTH = 1536
WINDOW_HEIGHT = 1000

def make_grass():
    grass_list = arcade.SpriteList()
    for xLoc in range(64, WINDOW_WIDTH, 128): #64 is center of first block, 128 is size of block
        grass_block = arcade.Sprite(":resources:images/tiles/grassMid.png")
        grass_block.center_y = 64
        grass_block.center_x = xLoc
        grass_list.append(grass_block)
    return grass_list

class FirstWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "First Real Arcade")
        self.player = None
        self.target = None
        self.score = 0
        self.ground = None

    def setup(self):
        self.player = arcade.Sprite(":resources:images/enemies/frog.png")
        self.player.center_x = 100
        self.player.center_y = 200
        self.target = arcade.Sprite(":resources:images/enemies/fly.png")
        self.target.center_x = random.randint(0, WINDOW_WIDTH)
        self.target.center_y = random.randint(WINDOW_HEIGHT/2, WINDOW_HEIGHT)
        self.ground = make_grass()

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(0,0,WINDOW_WIDTH, WINDOW_HEIGHT/2,
                                          arcade.color.OLIVE)
        arcade.draw_xywh_rectangle_filled(0, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT/2,
                                          arcade.color.BLUE)
        self.ground.draw()
        self.player.draw()
        self.target.draw()
        arcade.finish_render()


