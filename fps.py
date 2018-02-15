import pygame


class fps_limiter:

    def __init__(self):
        self.FPS = 60
        self.TIME_PER_FRAME = 1000 / 60
        self.start_ticks = 0.0
        self.end_ticks = 0.0
        self.change_in_ticks = 0.0
        self.time_waited = 0.0

    def update_timer(self):
        self.start_ticks = pygame.time.get_ticks()

    def get_change_in_ticks(self):
        self.end_ticks = pygame.time.get_ticks()
        self.change_in_ticks = self.end_ticks - self.start_ticks
        return self.change_in_ticks

    def control_fps(self):
        delta_ticks = self.get_change_in_ticks()
        if delta_ticks < self.TIME_PER_FRAME:
            if delta_ticks < 11.0:
                self.time_waited = int(self.TIME_PER_FRAME - delta_ticks)
                pygame.time.wait(self.time_waited)
            else:
                self.time_waited = int(self.TIME_PER_FRAME - delta_ticks)
                pygame.time.delay(self.time_waited)
