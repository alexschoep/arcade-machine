
from arcade_machine.games.game import Game
from arcade_machine.sprites.label import Label
from pygame import font

class ArcadeSettings(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (0, 0, 0)

        self.TITLE_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 48)
        self.BODY_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 24)
        self.menu_title = Label('Settings', (255, 255, 255), 512, 60, None, self.TITLE_FONT)
        self.drawable_objects.append(self.menu_title)


        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass