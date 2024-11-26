from pico2d import *
import game_world
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(20, server.background.w-20)
        self.y = y if y else random.randint(20, server.background.h-20)

        self.sx = self.x
        self.sy = self.y
    def draw(self):
        self.image.draw(self.sx, self.sy)
        draw_rectangle(self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10)

    def update(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if 'boy:ball':
            game_world.remove_object(self)
