# This is the main class that "puts it all together" and manages all of the 
# objects directly related to the game window.

import pygame
from player import Player
from fps import fps_limiter
from collision import Collision



class Application:

    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.backgroundColor = (255, 255, 255)
        self.textColor = (0, 0, 0)

        self.is_running = True
        pygame.init()
        self.fps_controller = fps_limiter() # IMPORTANT - FPS Controller must be started AFTER the call to
                                            # pygame.init(). The timer in pygame gets the time in milliseconds
        self.up_pressed = False             # from the call to pygame.init().
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.pressed = None                 # Empty object to store output from pygame.key.get_pressed()

        self.up = pygame.K_UP               # Key constants redefined for easier typing
        self.down = pygame.K_DOWN
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.space = pygame.K_SPACE

        # Setup for the screen, background, and player objects
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background.fill(self.backgroundColor, None)
        self.player = Player("Gjiorgisborgen")
        self.player.setup_entity(400, 400, 30, 30)

        # Font initialization
        pygame.font.init()
        self.text_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

        # Text Surface initial render
        self.player_info = self.text_font.render(self.player.__str__(), True, (0, 0, 0))

        # Collision detection object
        self.collision_checker = Collision(self.player)

    # Text update handling
    def update_text(self):
        self.player_info = self.text_font.render(self.player.__str__(), True, (0, 0, 0))
    # Main game loop function
    def main(self):

        while self.is_running:
            self.fps_controller.update_timer()
            self.event_loop()
            self.collision_checker.check_collision()
            self.player.updateEntity()
            self.fps_controller.control_fps()
            self.render()
            pygame.display.flip()

    def getscreen(self):
        return self.screen

    # ALL RENDERING DONE HERE!!!
    def render(self):
        pygame.draw.rect(self.screen, self.backgroundColor, pygame.Rect(0, 0, 800, 600), 800)
        self.player.drawEntity(self.getscreen())
        self.update_text()
        self.screen.blit(self.player_info, (0, 0))

    # The event loop first uses get_pressed()->[]Booleans, which represent the overall
    # state of every key on the keyboard. It's from this new self.pressed variable that
    # we store the states that we care about, up down left and right, in single, easily accessible
    # Boolean variables. These are then changed within the loop itself based on the input from
    # the use.
    def event_loop(self):

        self.pressed = pygame.key.get_pressed()             # Get the key states

        self.up_pressed = self.pressed[self.up]             # Update the key states
        self.down_pressed = self.pressed[self.down]
        self.left_pressed = self.pressed[self.left]
        self.right_pressed = self.pressed[self.right]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit_application()

            if event.type == pygame.KEYDOWN:
                if event.key == self.up:
                    self.player.set_y_vel(-3)
                    self.up_pressed = True

                if event.key == self.down:
                    self.player.set_y_vel(3)
                    self.down_pressed = True
                if event.key == self.left:
                    self.player.set_x_vel(-3)
                    self.left_pressed = True
                if event.key == self.right:
                    self.player.set_x_vel(3)
                    self.right_pressed = True

                if event.key == self.space:
                    if not self.player.get_jump_started() or self.player.get_y() == (self.collision_checker.maxy - 1):
                        self.player.set_y_vel(-10)
                        self.player.set_y_accel(0.5)
                        self.player.set_jump_started(True)

            if event.type == pygame.KEYUP:
                if event.key == self.up and self.down_pressed:
                    self.player.set_y_vel(3)
                    self.up_pressed = False
                elif event.key == self.up:
                    self.player.set_y_vel(0)
                    self.up_pressed = False
                if event.key == self.down and self.up_pressed:
                    self.player.set_y_vel(-3)
                    self.down_pressed = False
                elif event.key == self.down:
                    self.player.set_y_vel(0)
                    self.down_pressed = False

                if event.key == self.left and self.right_pressed:
                    self.player.set_x_vel(3)
                    self.left_pressed = False
                elif event.key == self.left:
                    self.player.set_x_vel(0)
                    self.left_pressed = False
                if event.key == self.right and self.left_pressed:
                    self.player.set_x_vel(-3)
                    self.right_pressed = False
                elif event.key == self.right:
                    self.player.set_x_vel(0)
                    self.right_pressed = False

    def quit_application(self):
        pygame.font.quit()
        pygame.quit()




































