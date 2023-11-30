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
        self.dx = 0
        self.ouch = False
        self.hit_sound = None
        self.lives = 5
        self.shots = arcade.SpriteList()

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
        if symbol == arcade.key.LEFT:
            self.dx = -2
        elif symbol == arcade.key.RIGHT:
            self.dx = 2

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.dy = 0
        elif symbol == arcade.key.DOWN:
            self.dy = 0
        if symbol == arcade.key.LEFT:
            self.dx = 0
        elif symbol == arcade.key.RIGHT:
            self.dx = 0
        if symbol == arcade.key.SPACE:
            new_shot = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
            new_shot.center_y = self.player.center_y
            new_shot.center_x = self.player.center_x+new_shot.width
            self.shots.append(new_shot)

    def on_update(self, delta_time: float):
        if self.lives <=0:
            return
        self.player.center_y +=self.dy
        if self.player.center_y >=WINDOW_HEIGHT:
            self.player.center_y = WINDOW_HEIGHT
        elif self.player.center_y <= 0:
            self.player.center_y = 0
        self.player.center_x += self.dx
        if self.player.center_x >= WINDOW_WIDTH:
            self.player.center_x = WINDOW_WIDTH
        elif self.player.center_x <= 0:
            self.player.center_x = 0
        for rock in self.rocks:
            rock.center_x -=2
            if rock.center_x <= -rock.width/2:
                rock.center_x = WINDOW_WIDTH+64
        for shot in self.shots:
            shot.center_x +=2
            if shot.center_x > WINDOW_WIDTH:
                self.shots.remove(shot)
        if arcade.check_for_collision_with_list(self.player, self.rocks):
            self.ouch = True
            self.lives -=1
            arcade.play_sound(self.hit_sound)
            self.player.center_y = random.randint(self.player.height, WINDOW_HEIGHT)
        for shot in self.shots:
            hit_rocks = arcade.check_for_collision_with_list(shot, self.rocks)
            if hit_rocks:
                self.shots.remove(shot)
                self.rocks.remove(hit_rocks[0])


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.rocks.draw()
        self.shots.draw()
        if self.lives <=0:
            message = arcade.Text("GAME OVER", WINDOW_WIDTH/3, WINDOW_HEIGHT*.75, arcade.color.YELLOW, 30)
            message.draw()
            self.ouch = False
        arcade.finish_render()

def main():
    window2 = SpaceWindow()
    window2.setup()
    arcade.run()

main()

