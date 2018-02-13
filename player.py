from entity import Entity
from movable import Movable
import pygame


class Player(Entity, Movable):

    def __init__(self, name):
        Movable.__init__(self)
        Entity.__init__(self, name)
        self.color = (0, 0, 0)
        self.health = 100
        self.set_x(200)
        self.set_y(200)
        self.jump_started = False
        self.maxy = 600 - (self.get_width() + 15)
        self.touched_ground = False

    def setup_entity(self, xpos, ypos, height, width):
        self.set_x(xpos)
        self.set_y(ypos)
        self.set_height(height)
        self.set_width(width)

    def drawEntity(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xPosition, self.yPosition, 30, 30), 30)

    def processEvents(self):
        pass

    def updateEntity(self):
        self.x_vel += self.x_accel
        self.y_vel += self.y_accel

        self.xPosition += self.x_vel
        self.yPosition += self.y_vel


    def jump(self):
        self.set_jump_started(True)
        self.set_y_accel(-1)

    def set_jump_started(self, is_started):
        self.jump_started = is_started

    def get_jump_started(self):
        return self.jump_started

    def update_x_pos(self):
        self.xPosition *= self.get_x_vel()

    def update_y_pos(self):
        self.yPosition *= self.get_y_vel()

    def update_y_vel(self, newyvel):
        self.y_vel = newyvel

    def update_x_vel(self, newxvel):
        self.x_vel = newxvel

    def __str__(self):
        return super(Player, self).__str__() + "X_VEL: {0}  ".format(self.x_vel) + "Y_VEL: {0}  ".format(self.y_vel) \
                                             + "X_ACCEL: {0} ".format(self.get_x_accel()) + "Y_ACCEL: {0}  ".format(self.get_y_accel())

