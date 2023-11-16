import arcade

WINDOW_WIDTH = 1536
WINDOW_HEIGHT = 1000
class FirstWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "First Real Arcade")
        self.player = None
        self.target = None
        self.score = 0

    def setup(self):
        self.player = arcade.Sprite(":resources:images/enemies/frog.png")
        self.player.center_x = 100
        self.player.center_y = 200
        self.target = arcade.Sprite(":resources:images/enemies/fly.png")
        self.target.center_x = 1000
        self.target.center_y = 800

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(0,0,WINDOW_WIDTH, WINDOW_HEIGHT/2,
                                          arcade.color.OLIVE)
        self.player.draw()
        self.target.draw()
        arcade.finish_render()


