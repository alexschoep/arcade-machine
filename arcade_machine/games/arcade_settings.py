
from arcade_machine.games.game import Game
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.controllers.music_player import set_volume, get_volume
from arcade_machine.events import CHANGE_GAME
from pygame import font
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

        self.settings_title = Label('Settings', (255, 255, 255), 512, 60, self.TITLE_FONT)
        self.vol_text = Label('System Volume:', (255, 255, 255), 512, 200, self.BODY_FONT)
        self.vol_level = Label(str(int(self.volume * 100)), (255, 255, 255), 512, 250, self.BODY_FONT)
        self.ver_text = Label('Version 0.0.1', (100, 100, 100), 512, 400, self.BODY_FONT)
        self.back = Label("Press 'A' to return to the games.", (120, 120, 120), 512, 530, self.BODY_FONT)
        self.leave = Label('Press MENU to quit the console.', (80, 10, 15), 512, 575, self.BODY_FONT)
        self.creators = Label('By Alex and Billy', (40, 40, 40), 512, 670, self.BODY_FONT)

        self.drawable_objects.append(self.settings_title) # Add labels to be drawn
        self.drawable_objects.append(self.vol_text)
        self.drawable_objects.append(self.vol_level)
        self.drawable_objects.append(self.ver_text)
        self.drawable_objects.append(self.back)
        self.drawable_objects.append(self.leave)
        self.drawable_objects.append(self.creators)

        self.divider = Rectangle(color=(255, 255, 255),
                                     x_pos=0,
                                     y_pos=120,
                                     width=1024,
                                     height=4,
                                     line_weight=4,
                                     bevel=0,
                                     alpha=255,
                                     anchor="TopLeft")
        self.drawable_objects.append(self.divider)

        self.bar_outline = Rectangle(color=(65, 65, 65),
                                      x_pos=512,
                                      y_pos=290,
                                      width=800,
                                      height=30,
                                      line_weight=2,
                                      bevel=5,
                                      alpha=255,
                                      anchor="Center")
        self.drawable_objects.append(self.bar_outline)

        self.fill_bar = Rectangle(color=(10, 80, 65),
                                     x_pos=116,
                                     y_pos=290,
                                     width=int(self.volume * 792),
                                     height=22,
                                     line_weight=0,
                                     bevel=3,
                                     alpha=255,
                                     anchor="MidLeft")
        self.drawable_objects.append(self.fill_bar)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_j:
                self.handle_change_volume('DOWN')
            elif event.key == K_d or event.key == K_l:
                self.handle_change_volume("UP")
            elif event.key == K_1 or event.key == K_9:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
            elif event.key == K_m:
                pygame_quit()
                exit()
    def update(self):
        pass

    def handle_change_volume(self, delta):
        if delta == "UP":
            self.volume += 0.05
        else:
            self.volume -= 0.05
        if self.volume > 1.0:  # Ensure the volume level is in the pygame mixer limits
            self.volume = 1.0
        elif self.volume < 0:
            self.volume = 0

        set_volume(self.volume)

        self.vol_level.redraw_label(text=str(int(self.volume * 100)))
        self.fill_bar.change_rectangle_dimension(int(self.volume * 792), 22)
