from player import Player


class Collision:

    def __init__(self, player: Player):
        self.playerref = player
        self.minx = 15
        self.miny = 15
        self.maxx = 800 - (self.playerref.get_width() + 15)  # The "+ 15" is there because of
        self.maxy = 600 - (self.playerref.get_width() + 15)  # weirdness with the way the player
                                                             # rect is drawn.
    def check_collision(self):
        collision = False
        if self.playerref.get_x() <= self.minx:
            self.playerref.set_x_vel(0)
            self.playerref.set_x(self.playerref.get_x() + 1)
            collision = True


        elif self.playerref.get_x() >= self.maxx:
            self.playerref.set_x_vel(0)
            self.playerref.set_x(self.playerref.get_x() - 1)
            collision = True

        elif self.playerref.get_y() < self.miny:
            self.playerref.set_y_vel(1)
            self.playerref.set_y_accel(1)
            self.playerref.set_y(self.miny + 1)
            collision = True

        elif self.playerref.get_y() >= self.maxy:
            self.playerref.set_y_vel(0)
            self.playerref.set_y_accel(0)
            self.playerref.set_y(self.maxy - 1)
            collision = True


        # self.gravity_checker()
        return collision

    def gravity_checker(self):
        if self.playerref.get_y() == (self.maxy - 1):
            self.playerref.set_y_accel(0)
            self.playerref.jump_started = False
            self.playerref.touched_ground = True

        elif self.playerref.get_y() > (self.maxy - 1):
            self.playerref.set_y_accel(-1)
