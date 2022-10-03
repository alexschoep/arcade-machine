
from pygame import KEYDOWN, K_m, K_p, K_1, K_8, K_w, K_a, K_s, K_d, K_i, K_j, K_k, K_l
import string
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from pygame.event import post as pygame_post_event
from pygame.event import Event
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.label import Label
from arcade_machine.high_score_manager import high_score_manager
from arcade_machine.font_manager import font_manager
from arcade_machine.components.carousel_menu import CarouselMenu

from random import randint

class Anaconda():
    def __init__(self):
        self.pieces = [(503, 354), (503, 374), (503, 394)] # Make 3 lined up in center
        self.direction = 'North'
        self.pacer = 5
        self.collide = False
        self.length = 3

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

            if len(self.pieces) > self.length:
                self.pieces.pop()

        self.collide = self.check_body_collision()
        self.pacer = self.inc_difficulty()

    def check_body_collision(self):
        if self.pieces.count(self.pieces[0]) > 1:
            return True
        if self.pieces[0][0] < 262:
            return True
        elif self.pieces[0][0] > 762:
            return True
        elif self.pieces[0][1] < 134:
            return True
        elif self.pieces[0][1] > 614:
            return True
        return False

    def inc_difficulty(self):
        if self.length > 50:
            return 1
        elif self.length > 20:
            return 2
        elif self.length > 10:
            return 3
        return 5

class Fruit():
    def __init__(self):
        colors = [
            (200, 0, 0), # Red
            (234, 119, 18), # Orange
            (234, 221, 18), # Yellow
            (18, 163, 28), # Green
            (54, 209, 226), # Teal
            (24, 110, 198), # Blue
            (153, 54, 226), # Purple
            (226, 54, 177) # Pink
        ]
        x_pos = (randint(0,24) * 20) + 263
        y_pos = (randint(0,24) * 20) + 134
        self.pos = (x_pos, y_pos)
        self.color = colors[randint(0,7)]

    def update(self):
        pass

class Snake(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.game_state = 'START'
        self.background = (121, 120, 156)
        self.frame_counter = 0
        self.game_score = 3
        self.num_fruit = 0
        self.body_sprite_group = Group()
        self.fruit_sprite_group = Group()

        self.header_font = font_manager.get_font("early_gameboy", 72)
        self.large_font = font_manager.get_font("early_gameboy", 48)
        self.body_font = font_manager.get_font("early_gameboy", 24)
        self.small_font = font_manager.get_font("early_gameboy", 12)

        self.sel_option = 'Play'
        self.initials_position = 0
        self.alphabet = list(string.ascii_uppercase)
        self.carousel_initials_0 = CarouselMenu(self.alphabet)
        self.carousel_initials_1 = CarouselMenu(self.alphabet)
        self.carousel_initials_2 = CarouselMenu(self.alphabet)

        # Start Screen View widgets
        self.title_label = Label('SNAKE', (62, 59, 156), 512, 180, self.header_font)
        self.play_label = Label('PLAY', (0,0,0), 512, 460, self.large_font)
        self.menu_label = Label('EXIT', (180, 180, 180), 512, 540, self.large_font)
        self.label_highlight = Rectangle(color=(62, 59, 156),
                                         x_pos=512,
                                         y_pos=460,
                                         width=280,
                                         height=80,
                                         line_weight=0,
                                         bevel=8,
                                         alpha=255,
                                         anchor="Center")

        # Game Play View widgets
        self.anaconda = Anaconda()
        self.fruit = Fruit()
        self.play_area = Rectangle(color=(8, 10, 20),
                                    x_pos=512,
                                    y_pos=384,
                                    width=500,
                                    height=500,
                                    line_weight=0,
                                    bevel=3,
                                    alpha=255,
                                    anchor="Center")
        self.score_label = Label('3', (180, 180, 180), 762, 110, self.body_font)

        # Game Over Widgets
        self.game_over_label = Label('GAME OVER', (62, 59, 156), 512, 70, self.large_font)
        self.continue_label = Label("Press 'A' to continue.", (62, 59, 156), 512, 700, self.body_font)

        self.high_score_label = Label('High Scores', (62, 59, 156), 512, 70, self.large_font)
        self.enter_high_score_label = Label('Enter your initials below', (62, 59, 156), 512, 150, self.body_font)
        self.high_score_initial_0 = Label(self.carousel_initials_0.get_selected_item(), (62, 59, 156), 412, 400, self.header_font)
        self.high_score_initial_1 = Label(self.carousel_initials_1.get_selected_item(), (62, 59, 156), 512, 400, self.header_font)
        self.high_score_initial_2 = Label(self.carousel_initials_2.get_selected_item(), (62, 59, 156), 612, 400, self.header_font)

        self.top_high_score_label = Label("Person", (62, 59, 156), 512, 300, self.header_font)
        self.mid_high_score_label = Label("Person", (62, 59, 156), 512, 400, self.header_font)
        self.low_high_score_label = Label("Person", (62, 59, 156), 512, 500, self.header_font)

        self.start_screen_view()

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_m:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
                return
            if event.key == K_1 or event.key == K_8:
                if self.game_state == 'START':
                    if self.sel_option == 'Play':
                        self.game_state = 'GAME'
                        self.game_play_view()
                    elif self.sel_option == 'Menu':
                        event = Event(CHANGE_GAME, {"game": "MainMenu"})
                        pygame_post_event(event)
                        return
                elif self.game_state == 'OVER':
                    if self.check_scores():
                        self.game_state = 'HIGH'
                        self.high_score_entry_view()
                    else:
                        self.game_state = 'SCORE'
                        self.high_score_view()
                elif self.game_state == 'HIGH':
                    self.game_state = 'SCORE'
                    self.high_score_view()
                elif self.game_state == 'SCORE':
                    self.game_state = 'START'
                    self.start_screen_view()

            if event.key == K_w or event.key == K_i:
                if self.game_state == 'START':
                    self.sel_option = 'Play'
                elif self.game_state == 'GAME':
                    self.anaconda.direction = 'North'
                elif self.game_state == 'HIGH':
                    self.change_letter('UP')
            if event.key == K_a or event.key == K_j:
                if self.game_state == 'GAME':
                    self.anaconda.direction = 'West'
                elif self.game_state == 'HIGH':
                    self.initials_position -= 1
            if event.key == K_s or event.key == K_k:
                if self.game_state == 'START':
                    self.sel_option = 'Menu'
                elif self.game_state == 'GAME':
                    self.anaconda.direction = 'South'
                elif self.game_state == 'HIGH':
                    self.change_letter('DOWN')
            if event.key == K_d or event.key == K_l:
                if self.game_state == 'GAME':
                    self.anaconda.direction = 'East'
                elif self.game_state == 'HIGH':
                    self.initials_position += 1

    def update(self):
        if self.game_state == "START":
            self.start_screen_update()
        elif self.game_state == 'GAME':
            self.game_play_update()
        elif self.game_state == 'OVER':
            self.game_over_view()
        elif self.game_state == 'HIGH':
            self.high_score_entry_update()
        elif self.game_state == 'SCORE':
            pass

    def start_screen_view(self): # START
        self.drawable_objects.clear()
        self.drawable_objects.append(self.title_label)
        self.drawable_objects.append(self.label_highlight)
        self.drawable_objects.append(self.play_label)
        self.drawable_objects.append(self.menu_label)

    def start_screen_update(self):
        if self.sel_option == 'Play':
            self.label_highlight.change_rectangle_position(512, 460, "Center")
            self.play_label.redraw_label(color=(200, 200, 200))
            self.menu_label.redraw_label(color=(62, 59, 156))
        elif self.sel_option == 'Menu':
            self.label_highlight.change_rectangle_position(512, 540, "Center")
            self.play_label.redraw_label(color=(62, 59, 156))
            self.menu_label.redraw_label(color=(200, 200, 200))

    def game_play_view(self): # GAME
        self.anaconda = Anaconda()

        self.drawable_objects.clear()
        self.drawable_objects.append(self.play_area)
        self.drawable_objects.append(self.body_sprite_group)
        self.drawable_objects.append(self.fruit_sprite_group)
        self.drawable_objects.append(self.score_label) # GAME

    def game_play_update(self):
        self.frame_counter = (self.frame_counter + 1) % 30
        if self.anaconda.collide == True:
            self.game_state = 'OVER'

        self.collide_fruit()

        if self.num_fruit == 0:
            self.fruit_sprite_group.empty()
            self.fruit = Fruit()
            block = Rectangle(color=self.fruit.color,
                              x_pos=self.fruit.pos[0],  # x coord
                              y_pos=self.fruit.pos[1],  # y coord
                              width=19,
                              height=19,
                              line_weight=0,
                              bevel=3,
                              alpha=255,
                              anchor="TopLeft")
            self.fruit_sprite_group.add(block)
            self.num_fruit = 1

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

    def game_over_view(self): # OVER
        #self.drawable_objects.clear()
        self.drawable_objects.append(self.game_over_label)
        self.drawable_objects.append(self.continue_label)

    def high_score_entry_view(self): # HIGH
        self.drawable_objects.clear()
        self.drawable_objects.append(self.high_score_label)
        self.drawable_objects.append(self.enter_high_score_label)

        self.drawable_objects.append(self.high_score_initial_0)
        self.drawable_objects.append(self.high_score_initial_1)
        self.drawable_objects.append(self.high_score_initial_2)

        self.drawable_objects.append(self.continue_label)

    def high_score_entry_update(self):
        if self.initials_position < 0:
            self.initials_position = 0
        elif self.initials_position > 2:
            self.initials_position = 2

        if self.initials_position == 0:
            self.high_score_initial_0.redraw_label(text=self.carousel_initials_0.get_selected_item(), color=(255, 255, 255))
            self.high_score_initial_1.redraw_label(color=(62, 59, 156))
            self.high_score_initial_2.redraw_label(color=(62, 59, 156))
        elif self.initials_position == 1:
            self.high_score_initial_0.redraw_label(color=(62, 59, 156))
            self.high_score_initial_1.redraw_label(text=self.carousel_initials_1.get_selected_item(), color=(255, 255, 255))
            self.high_score_initial_2.redraw_label(color=(62, 59, 156))
        elif self.initials_position == 2:
            self.high_score_initial_0.redraw_label(color=(62, 59, 156))
            self.high_score_initial_1.redraw_label(color=(62, 59, 156))
            self.high_score_initial_2.redraw_label(text=self.carousel_initials_2.get_selected_item(), color=(255, 255, 255))

    def high_score_view(self): # SCORE

        print(high_score_manager.get_high_scores('Snake'))

        self.drawable_objects.clear()
        self.drawable_objects.append(self.high_score_label)

        self.drawable_objects.append(self.top_high_score_label)
        self.drawable_objects.append(self.mid_high_score_label)
        self.drawable_objects.append(self.low_high_score_label)

        self.drawable_objects.append(self.continue_label)

    def collide_fruit(self):
        if self.anaconda.pieces[0] == self.fruit.pos:
            self.num_fruit = 0
            self.anaconda.length += 1
            self.score_label.redraw_label(text=str(self.anaconda.length))

    def check_scores(self):
        return high_score_manager.check_if_high_score('Snake', self.game_score)

    def set_score(self):
        high_score_manager.new_high_score('Snake', str(self.high_score_initial_0 +
                                                       self.high_score_initial_1 +
                                                       self.high_score_initial_2),
                                                       self.game_score)

    def change_letter(self, movement):
        if movement == 'UP':
            if self.initials_position == 0:
                self.carousel_initials_0.select_previous_item()
            elif self.initials_position == 1:
                self.carousel_initials_1.select_previous_item()
            elif self.initials_position == 2:
                self.carousel_initials_2.select_previous_item()
        elif movement == 'DOWN':
            if self.initials_position == 0:
                self.carousel_initials_0.select_next_item()
            elif self.initials_position == 1:
                self.carousel_initials_1.select_next_item()
            elif self.initials_position == 2:
                self.carousel_initials_2.select_next_item()

    def reset(self):
        self.game_score = 0