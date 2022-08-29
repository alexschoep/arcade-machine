
from arcade_machine.games.game import Game
from arcade_machine.sprites.label import Label
from arcade_machine.components.music_player import music_volume, get_volume
from arcade_machine.components.shape_to_sprite import rect_sprite
from arcade_machine.events import CHANGE_GAME
from pygame import font
from pygame import draw
from pygame import KEYDOWN, K_a, K_d, K_j, K_l, K_1, K_9, K_m
from pygame import quit as pygame_quit
from pygame.event import post as pygame_post_event
from pygame.event import Event

class ArcadeSettings(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (0, 0, 0)
        self.volume = get_volume()

        self.TITLE_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 48)
        self.BODY_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 24)
        self.menu_title = Label('Settings', (255, 255, 255), 512, 60, None, self.TITLE_FONT)
        self.drawable_objects.append(self.menu_title)
        self.vol_text = Label('System Volume:', (255, 255, 255), 512, 200, None, self.BODY_FONT)
        self.drawable_objects.append(self.vol_text)
        self.vol_level = Label(str(int(self.volume * 100)), (255, 255, 255), 512, 250, None, self.BODY_FONT)
        self.drawable_objects.append(self.vol_level)
        self.ver_text = Label('Version 0.0.1', (100, 100, 100), 512, 400, None, self.BODY_FONT)
        self.drawable_objects.append(self.ver_text)
        self.back = Label("Press 'A' to return to the games.", (120, 120, 120), 512, 530, None, self.BODY_FONT)
        self.drawable_objects.append(self.back)
        self.leave = Label('Press MENU to quit the console.', (80, 10, 15), 512, 575, None, self.BODY_FONT)
        self.drawable_objects.append(self.leave)
        self.creators = Label('By Alex and Billy', (40, 40, 40), 512, 670, None, self.BODY_FONT)
        self.drawable_objects.append(self.creators)

        #self.line = rect_sprite((100, 0, 1024, 12))
        #self.drawable_objects.append(self.line)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_j:
                self.volume -= 0.05
            elif event.key == K_d or event.key == K_l:
                self.volume += 0.05
            elif event.key == K_1 or event.key == K_9:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
            elif event.key == K_m:
                pygame_quit()
                exit()
    def update(self):
        if self.volume > 1.0:
            self.volume = 1.0
        elif self.volume < 0:
            self.volume = 0
        music_volume(self.volume)

        self.drawable_objects.clear()

        self.drawable_objects.append(self.menu_title)
        self.drawable_objects.append(self.vol_text)
        self.vol_level = Label(str(int(self.volume * 100)), (255, 255, 255), 512, 250, None, self.BODY_FONT)
        self.drawable_objects.append(self.vol_level)
        self.drawable_objects.append(self.ver_text)
        self.drawable_objects.append(self.back)
        self.drawable_objects.append(self.leave)
        self.drawable_objects.append(self.creators)