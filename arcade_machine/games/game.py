from abc import abstractmethod

from matplotlib.pyplot import title

class Game:
    def __init__(self):
        self.background = None
        self.drawable_objects = []

    @abstractmethod
    def initialize(self):
        raise NotImplementedError()

    @abstractmethod
    def handle_event(self, event):
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        raise NotImplementedError()

    def draw_screen(self, screen):
        screen.fill(self.background)
        for drawable_object in self.drawable_objects:
            drawable_object.draw(screen)
