## @package obstacles
import pyray as pr
import entity_manager.entity_manager as em

class Obstacle:
    def __init__(self, color, shape):
        self.entity = em.Entity(shape)
        self.color = color
    def draw(self):
        pr.draw_rectangle_rec(self.entity.shape.ctype(), self.color)
        #pr.draw_text(f"{self.entity.shape.x}, {self.entity.shape.y}", self.entity.shape.x, self.entity.shape.y, 10, pr.BLACK)


