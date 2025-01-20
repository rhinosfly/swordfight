## @package weapon
import entity_manager.entity_manager as em
import pyray as pr
from enum import Enum, auto
import entity_manager.shapes as shapes
import math
from globals import *

class State(Enum):
    NONE = 0 # not used
    UNOWNED = auto()
    OWNED = auto()
    SWING = auto()
    BLOCK = auto()

## recieve commands, and do motions
class Weapon:
    pass

## scope for now is just while held
class Sword(Weapon):
    def __init__(self, position, direction):
        self.length = SWORD_LENGTH
        self.position = position # axis position
        self.direction = direction # ie. left/right
        self.angle = self.set_angle(SWORD_ANGLE)
        self.color = pr.GRAY
        self.state = State.OWNED
        self.entity = em.Entity(Sword.get_points(self.position, self.length, self.angle))
    ## using position and length, return shapes.Line
    def get_points(position, length, angle):
        print(angle)
        p1 = position
        width = math.cos(angle) * length
        height = math.sin(angle) * length
        x2 = position.x + width
        y2 = position.y + height
        p2 = shapes.Point(x2,y2)
        line = shapes.Line(p1, p2)
        return line
    ## call to move sword to position
    def set_position(self, point):
        self.position = point
        return self.position
    def set_angle(self, angle):
        self.angle = angle * self.direction - math.pi/2
        return self.angle
    def set_direction(self, direction):
        self.direction = direction
        return self.direction
    ## update self
    def update(self):
        pass
    ## draw self
    def draw(self):
        pr.draw_line_v(self.entity.shape.p1.ctype(), self.entity.shape.p2.ctype(), self.color)
