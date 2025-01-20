## @package players
#
# the classes used by swordfight
import pyray as pr
import entity_manager.shapes as shapes
import entity_manager.entity_manager as em
from globals import *


class Player:
    def __init__(self, position, color, key_bindings):
        self.entity = em.Entity(shapes.Rectangle(position.x,position.y,PLAYER_WIDTH, PLAYER_HIGHT))
        self.color = color
        self.position = position
        self.key_bindings = key_bindings
        self.weapon = None

    ## move according to keypress
    def do_keypress_actions(self):
        if pr.is_key_down(self.key_bindings['up']):
            self.position.y -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['down']):
            self.position.y += PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['left']):
            self.position.x -= PLAYER_SPEED
        if pr.is_key_down(self.key_bindings['right']):
            self.position.x += PLAYER_SPEED
            
    ## update rectangle
    def update_entity(self):
        self.entity.shape.x = self.position.x
        self.entity.shape.y = self.position.y

    ## calculate and move for collisions
    def collide(self):
        edges = { 'up':0,'down':0,'left':0,'right':0 } # shows which edges have collided
        player = self.entity.shape
        # find which edges are hitting which shapes
        for overlap in self.entity.overlaps:
            shape = overlap.shape
            if not isinstance(shape, shapes.Rectangle):
                continue
            # find edge to edge distances in every direction
            buffer = { 'up':0,'down':0,'left':0,'right':0 } # buffer for edge distances for this overlap
            buffer['up'] = player.y + player.height - shape.y # distance moving down etc.
            buffer['down'] = shape.y + shape.height - player.y # distance to avoid overlap moving upward
            buffer['left'] = player.x + player.width - shape.x
            buffer['right'] = shape.x + shape.width - player.x
            # find shortest distance
            keys = sorted(buffer, key=buffer.get)
            key = None
            value = None
            for x in keys:
                if buffer[x]:
                    key = x
                    value = buffer[x]
                    break
            # add shortest distance to edges, if it is larger than previous
            if value > edges[key]:
                edges[key] = value
        
        if edges['left'] and edges['right']:
            pass
        elif edges['left']:
            self.position.x -= edges['left']
        elif edges['right']:
            self.position.x += edges['right']
        if edges['up'] and edges['down']:
            pass
        elif edges['up']:
            self.position.y -= edges['up']
        elif edges['down']:
            self.position.y += edges['down']
        

    ## update self
    def update(self, recalculate_overlaps):
        self.do_keypress_actions()
        self.update_entity()
        recalculate_overlaps()
        if len(self.entity.overlaps):
            self.collide()
        self.update_entity() 
       

    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        #pr.draw_text(f"{self.position.x}, {self.position.y}", self.position.x, self.position.y, 10, pr.BLACK)

