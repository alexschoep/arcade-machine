
from pygame import KEYDOWN, K_m, K_p, K_1, K_8, K_w, K_a, K_s, K_d, K_i, K_j, K_k, K_l
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from pygame.event import post as pygame_post_event
from pygame.event import Event
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.label import Label

from pygame.font import Font as PygameFont
from arcade_machine.fonts.system_fonts import EARLY_GAMEBOY_FONT

import random

class Anaconda():
    def __init__(self):
        self.pieces = [(263, 134), (243, 134), (223, 134)] # Make 3 lined up in center
        self.direction = 'South'
        self.pacer = 5

    def update(self, frames):
        if frames % self.pacer == 0:
            if self.direction == 'North':
                new_x = self.pieces[0][0]
                new_y = self.pieces[0][1] - 20
            elif self.direction == 'South':
                new_x = self.pieces[0][0]
                new_y = self.pieces[0][1] + 20
            elif self.direction == 'East':
                new_x = self.pieces[0][0] + 20
                new_y = self.pieces[0][1]
            elif self.direction == 'West':
                new_x = self.pieces[0][0] - 20
                new_y = self.pieces[0][1]
            self.pieces.insert(0, (new_x, new_y))
            self.pieces.pop()
            print(len(self.pieces))



class Snake(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.game_state = 'START'
        self.background = (121, 120, 156)
        self.frame_counter = 0
        self.game_score = 0
        self.body_sprite_group = Group()
        self.fruit_sprite_group = Group()

        self.header_font = PygameFont(EARLY_GAMEBOY_FONT.get_file_path(), 72)
        self.large_font = PygameFont(EARLY_GAMEBOY_FONT.get_file_path(), 48)
        self.body_font = PygameFont(EARLY_GAMEBOY_FONT.get_file_path(), 24)
        self.small_font = PygameFont(EARLY_GAMEBOY_FONT.get_file_path(), 12)

        # Start Screen View widgets
        self.title_label = Label('SNAKE', (62, 59, 156), 512, 180, self.header_font)
        self.play_label = Label('PLAY', (0,0,0), 512, 500, self.body_font)
        self.menu_label = Label('EXIT', (180, 180, 180), 512, 550, self.body_font)

        # Game Play View widgets
        self.anaconda = Anaconda()
        self.play_area = Rectangle(color=(8, 10, 20),
                                    x_pos=512,
                                    y_pos=384,
                                    width=500,
                                    height=500,
                                    line_weight=0,
                                    bevel=5,
                                    alpha=255,
                                    anchor="Center")
        self.score_label = Label('0', (180, 180, 180), 512, 550, self.body_font)

        self.start_screen_view()

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_m:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
            if event.key == K_1 or event.key == K_8:
                if self.game_state == 'START':
                    self.game_state = 'GAME'
                    self.game_play_view()
            if event.key == K_w or event.key == K_i:
                if self.game_state == 'GAME':
                    self.anaconda.direction = 'North'


    def update(self):
        self.frame_counter = (self.frame_counter + 1) % 30

        if self.game_state == 'GAME':
            self.body_sprite_group.empty()
            for piece in self.anaconda.pieces:
                block = Rectangle(color=(200, 200, 200),
                                  x_pos=piece[0],  # x coord
                                  y_pos=piece[1],  # y coord
                                  width=19,
                                  height=19,
                                  line_weight=0,
                                  bevel=3,
                                  alpha=255,
                                  anchor="TopLeft")
                self.body_sprite_group.add(block)


            self.anaconda.update(self.frame_counter)


    def start_screen_view(self):
        self.drawable_objects.clear()
        self.drawable_objects.append(self.title_label)
        self.drawable_objects.append(self.play_label)
        self.drawable_objects.append(self.menu_label)

    def game_play_view(self):
        self.anaconda = Anaconda()

        self.drawable_objects.clear()
        self.drawable_objects.append(self.play_area)
        self.drawable_objects.append(self.body_sprite_group)


    def game_over_view(self):
        pass

    def high_score_entry_view(self):
        pass

    def high_score_view(self):
        pass