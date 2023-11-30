import random

import arcade
from SpaceHelpers import WINDOW_WIDTH
from SpaceHelpers import WINDOW_HEIGHT
import SpaceHelpers
class SpaceWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Space This time")
        self.player:arcade.Sprite = None
        self.rocks = None
        self.dy = 0
        self.ouch = False
        self.hit_sound = None


    def setup(self):
        self.player = arcade.Sprite("Blue-05.png")
        self.player.scale = 2
        self.player.center_x = 100
        self.player.center_y = WINDOW_HEIGHT/2
        self.rocks = SpaceHelpers.make_rocks()
        self.hit_sound = arcade.load_sound(":resources:sounds/hurt1.wav")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.DOWN:
            self.dy = -2
        elif symbol == arcade.key.UP:
            self.dy = 2

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.dy = 0
        elif symbol == arcade.key.DOWN:
            self.dy = 0

    def on_update(self, delta_time: float):
        self.player.center_y +=self.dy
        if self.player.center_y >=WINDOW_HEIGHT:
            self.player.center_y = WINDOW_HEIGHT
        elif self.player.center_y <= 0:
            self.player.center_y = 0
        for rock in self.rocks:
            rock.center_x -=2
            if rock.center_x <= -rock.width/2:
                rock.center_x = WINDOW_WIDTH+64
        if arcade.check_for_collision_with_list(self.player, self.rocks):
            self.ouch = True
            arcade.play_sound(self.hit_sound)
            self.player.center_y = random.randint(self.player.height, WINDOW_HEIGHT)


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.rocks.draw()
        if self.ouch:
            message = arcade.Text("OUCH!!!", WINDOW_WIDTH/3, WINDOW_HEIGHT*.75, arcade.color.YELLOW, 30)
            message.draw()
            self.ouch = False
        arcade.finish_render()

def main():
    window2 = SpaceWindow()
    window2.setup()
    arcade.run()

main()

