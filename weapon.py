## @package weapon
import entity_manager.entity_manager as em
import pyray as pr
from enum import Enum, auto
import entity_manager.shapes
import math
from globals import *

class State(Enum):
    NONE = 0 # not used
    UNOWNED = auto()
    OWNED = auto()
    SWING = auto()
    BLOCK = auto()
LEFT = -1
RIGHT = 1

## recieve commands, and do motions
class weapon:
    pass

## scope for now is just while held
class sword(weapon):
    def __init__(self, position, direction):
        self.length = SWORD_LENGTH
        self.position = position # axis position
        self.angle = SWORD_ANGLE
        self.direction = direction # ie. left/right
        self.color = pr.GRAY
        self.state = State.OWNED
        self.entity = em.Entity(self.get_points(self.position, self.length, self.angle))
    ## using position and length, return shapes.Line
    def get_points(position, length, angle):
        p1 = position
        width = math.cos(angle) * length
        hight = math.sin(angle) * length
        x2 = position.x + width
        y2 = position.y + height
        p2 = shapes.Point(x2,y2)
        line = shapes.Line(p1, p2)
        return line
    ## call to move sword to position
    def set_position(point):
        self.position = point
    def set_angle(angle):
        self.angle = angle * self.direction
    def set_direction(direction):
        self.direction = direction
    ## update self
    def update(self):
        pass
    ## draw self
    def draw(self):
        pr.draw_line_v(self.entity.shape.p1.ctype(), self.entity.shape.p2.ctype(), self.color)
