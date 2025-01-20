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
        self.entity = em.Entity(shapes.Rectangle(position.x,position.y,PLAYER_WIDTH, PLAYER_HIGHT))
        self.color = color
        self.position = position
        self.key_bindings = key_bindings

    def update(self):
        edges = { 'up':-1,'down':-1,'left':-1,'right':-1 } # shows which edges have collided
        # account for overlap (collisions)
        if len(self.entity.overlaps) > 0:
            player = self.entity.shape
            # find which edges are hitting which shapes
            for overlap in self.entity.overlaps:
                shape = overlap.shape.smallest_rect()
                if (shape.x == player.x) and (shape.width > edges['left']) and shape.height:
                    edges['left'] = shape.width
                if (shape.x + shape.width == player.x + player.width) and (shape.width > edges['right']) and shape.height:
                    edges['right'] = shape.width
                if (shape.y == player.y) and (shape.height > edges['up']) and shape.width:
                    edges['up'] = shape.height
                if (shape.y + shape.height == player.y + player.height) and (shape.height > edges['down']) and shape.width:
                    edges['down'] = shape.height
            # move accordingly
            if edges['left'] > -1 and edges['right'] > -1:
                pass
            elif edges['left'] > -1:
                self.position.x += edges['left']
            elif edges['right'] > -1:
                self.position.x -= edges['right']
            if edges['up'] > -1 and edges['down'] > -1:
                pass
            elif edges['up'] > -1:
                self.position.y += edges['up']
            elif edges['down'] > -1:
                self.position.y -= edges['down']
       # move according to keypress
        if pr.is_key_down(self.key_bindings['up']) and edges['up'] == -1:
            self.position.y -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['down']) and edges['down'] == -1:
            self.position.y += PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['left']) and edges['left'] == -1:
            self.position.x -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['right']) and edges['right'] == -1:
            self.position.x += PLAYER_SPEED
        # update rectangle
        self.entity.shape.x = self.position.x
        self.entity.shape.y = self.position.y

    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        pr.draw_text(f"{self.position.x}, {self.position.y}", self.position.x, self.position.y, 10, pr.BLACK)

class Obstacle:
    def __init__(self, color, shape):
        self.entity = em.Entity(shape)
        self.color = color
    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        pr.draw_text(f"{self.entity.shape.x}, {self.entity.shape.y}", self.entity.shape.x, self.entity.shape.y, 10, pr.BLACK)


