## @package classes
#
# the classes used by swordfight
import pyray as pr
import entity_manager.shapes as shapes
import entity_manager.entity_manager as em

#constants
PLAYER_WIDTH = 20
PLAYER_HIGHT = 60
PLAYER_SPEED = 3

class Player:
    def __init__(self, position, color, key_bindings):
        self.entity = em.Entity(shapes.Rectangle(None,None,PLAYER_WIDTH, PLAYER_HIGHT))
        self.color = color
        self.position = position
        self.key_bindings = key_bindings

    def update(self):
        if pr.is_key_down(self.key_bindings['up']):
            self.position.y -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['down']):
            self.position.y += PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['left']):
            self.position.x -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['right']):
            self.position.x += PLAYER_SPEED
        self.entity.shape.x = self.position.x
        self.entity.shape.y = self.position.y

    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)

class Obstacle:
    def __init__(self, color, shape):
        self.entity = em.Entity(shape)
        self.color = color
    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)


