import abc


class Movable:
    def __init__(self):
        self.x_vel = 0
        self.y_vel = 0
        self.x_accel = 0
        self.y_accel = 1

    def get_x_vel(self):
        return self.x_vel
    def get_x_accel(self):
        return self.x_accel
    def get_y_vel(self):
        return self.y_vel
    def get_y_accel(self):
        return self.y_accel
    def set_x_vel(self, xvel):
        self.x_vel = xvel
    def set_x_accel(self, xaccel):
        self.x_accel = xaccel
    def set_y_vel(self, yvel):
        self.y_vel = yvel
    def set_y_accel(self, yaccel):
        self.y_accel = yaccel
    # These are made abstract mainly for future
    # physics improvements in the engine. Right
    # now they are pretty bland.
    @abc.abstractmethod
    def update_x_pos(self):
        pass

    @abc.abstractmethod
    def update_y_pos(self):
        pass

    @abc.abstractmethod
    def update_y_vel(self, newyvel):
        pass

    @abc.abstractmethod
    def update_x_vel(self, newxvel):
        pass
