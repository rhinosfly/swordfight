## @package classes
#
# the classes used by swordfight
import pyray as pr
import entity_manager.shapes as shapes
import entity_manager.entity_manager as em

#constants
PLAYER_WIDTH = 20
PLAYER_HIGHT = 60
PLAYER_SPEED = 5

class Player:
    def __init__(self, position, color, key_bindings):
        self.entity = em.Entity(shapes.Rectangle(position.x,position.y,PLAYER_WIDTH, PLAYER_HIGHT))
        self.color = color
        self.position = position
        self.key_bindings = key_bindings

    def update(self, recalculate_func):
        # move according to keypress
        if pr.is_key_down(self.key_bindings['up']):
            self.position.y -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['down']):
            self.position.y += PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['left']):
            self.position.x -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['right']):
            self.position.x += PLAYER_SPEED
        # update rectangle
        self.entity.shape.x = self.position.x
        self.entity.shape.y = self.position.y
        # recalculate overlaps
        recalculate_func()
        edges = { 'up':0,'down':0,'left':0,'right':0 } # shows which edges have collided
        # account for overlap (collisions)
        if len(self.entity.overlaps):
            player = self.entity.shape
            # find which edges are hitting which shapes
            for overlap in self.entity.overlaps:
                shape = overlap.shape
                if not isinstance(shape, shapes.Rectangle):
                    continue
                if (shape.x == player.x) and (shape.width > edges['left']):
                    edges['left'] = shape.width
                if (shape.x + shape.width == player.x + player.width) and (shape.width > edges['right']):
                    edges['right'] = shape.width
                if (shape.y == player.y) and (shape.height > edges['up']):
                    edges['up'] = shape.height
                if (shape.y + shape.height == player.y + player.height) and (shape.height > edges['down']):
                    edges['down'] = shape.height
            # move accordingly
            if edges['left'] and edges['right']:
                pass
            elif edges['left']:
                self.position.x += edges['left']
            elif edges['right']:
                self.position.x -= edges['right']
            if edges['up'] and edges['down']:
                pass
            elif edges['up']:
                self.position.y += edges['up']
            elif edges['down']:
                self.position.y -= edges['down']
        # update rectangle
        self.entity.shape.x = self.position.x
        self.entity.shape.y = self.position.y
       

    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        #pr.draw_text(f"{self.position.x}, {self.position.y}", self.position.x, self.position.y, 10, pr.BLACK)

class Obstacle:
    def __init__(self, color, shape):
        self.entity = em.Entity(shape)
        self.color = color
    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        #pr.draw_text(f"{self.entity.shape.x}, {self.entity.shape.y}", self.entity.shape.x, self.entity.shape.y, 10, pr.BLACK)


