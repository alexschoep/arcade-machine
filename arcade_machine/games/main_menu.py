from pygame.event import post as pygame_post_event
from pygame.event import Event

from arcade_machine.controllers.music_player import load_music, play_music, stop_music
from arcade_machine.utility.color_blender import get_blended_colors_list
from arcade_machine.components.carousel_menu import CarouselMenu
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.components.game_thumbnail import *

class MainMenu(Game):
    def __init__(
        self
    ):
        super().__init__()

    def initialize(self):
        self.bg_animation_timer = 0
        self.bg_animation_steps = 8
        self.bg_color_list = [(0, 0, 0)]

        self.background = (0, 0, 0)

        self.font_eg_48 = font_manager.get_font("early_gameboy", 48)
        self.menu_title = Label('Arcade Machine', (255, 255, 255), 512, 60, self.font_eg_48)
        self.drawable_objects.append(self.menu_title)

        self.carousel_menu = CarouselMenu([
            asteroid_universe_thumbnail_item,
            snake_thumbnail_item,
            pong_thumbnail_item,
            mars_lander_thumbnail_item,
        ])

        self.drawable_objects.extend(
            self.carousel_menu.get_selected_item().get_drawable()
        )

        load_music('arcade_machine/resources/audio/Main_Menu/Theme.mp3')
        play_music()  # loop indefinitely
        self.update_colors_list()

    def handle_event(self, event):
        if event == 'P1_W_DOWN' or event == 'P2_W_DOWN':
            self.carousel_menu.select_next_item()
            self.replace_drawable()
            self.update_colors_list()
        elif event == 'P1_E_DOWN' or event == 'P2_E_DOWN':
            self.carousel_menu.select_previous_item()
            self.replace_drawable()
            self.update_colors_list()
        elif event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
            stop_music()
            event = Event(
                CHANGE_GAME,
                {"game": self.carousel_menu.get_selected_item().get_title()}
            )
            pygame_post_event(event)
        elif event == 'MENU_DOWN':
            stop_music()
            event = Event(CHANGE_GAME, {"game": "Settings"})
            pygame_post_event(event)

    def update(self):
        if self.bg_animation_timer <= self.bg_animation_steps: # Control the bg color change
            self.background = self.bg_color_list[self.bg_animation_timer]
            self.bg_animation_timer += 1

    def replace_drawable(self):
        self.drawable_objects = []
        self.drawable_objects.append(self.menu_title)
        self.drawable_objects.extend(
            self.carousel_menu.get_selected_item().get_drawable()
        )
    
    def update_colors_list(self):
        self.bg_color_list = get_blended_colors_list(
            self.background,
            self.carousel_menu.get_selected_item().get_bg_color(),
            self.bg_animation_steps
        )
        self.bg_animation_timer = 0
