import abc


class Entity:

    xPosition = 0
    yPosition = 0
    height = 0
    width = 0
    name = ""

    def __init__(self, name):
        self.name = name

    # Standard Getters and Setters for all of the
    # Entity's attributes

    def get_x(self):
        return self.xPosition

    def get_y(self):
        return self.yPosition

    def set_x(self, x_pos):
        self.xPosition = x_pos

    def set_y(self, y_pos):
        self.yPosition = y_pos

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    # Abstract method declarations
    @abc.abstractmethod
    def __str__(self):
        return "X_POS: {0}  ".format(self.xPosition) + "Y_POS: {0}  ".format(self.yPosition) \
                + "HEIGHT: {0}  ".format(self.height) + "WIDTH: {0}  ".format(self.width)

    @abc.abstractmethod
    def draw_entity(self, screen):
        pass

    @abc.abstractmethod
    def process_events(self):
        pass

    @abc.abstractmethod
    def update_entity(self):
        pass