import pygame.sprite
from pygame import KEYDOWN, K_a, K_d, K_j, K_l, K_ESCAPE, K_m, K_1, K_9
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame import quit as pygame_quit
from pygame import font

from arcade_machine.controller.music_player import load_music, play_music, stop_music
from arcade_machine.components.game_title import GameTitle
from arcade_machine.utility.color_blender import get_blended_colors_list
from arcade_machine.components.carousel import Carousel

from arcade_machine.events import CHANGE_GAME
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.image import Image
from arcade_machine.games.game import Game

from arcade_machine.resources.game_information import game_information

class MainMenu(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.animation_timer = 10 # Used for bg coloring
        self.animation_steps = 8
        self.color_list = [(0, 0, 0)] # Used for bg coloring

        self.TITLE_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 48)
        self.BODY_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 24)

        self.menu_title = Label('Arcade Machine', (255, 255, 255), 512, 60, None, self.TITLE_FONT)
        self.drawable_objects.append(self.menu_title)

        self.carousel = Carousel()
        self.list_o_games = game_information.list_of_game_information

        for game in self.list_o_games:
            new_game = GameTitle(game[0], game[1], game[2], game[3], game[4], game[5])
            self.carousel.add_object(new_game)

        self.background = self.carousel.objects[self.carousel.current_object].bg_color

        self.game_poster = Image(self.carousel.objects[self.carousel.current_object].poster,
                                 512, 360,
                                 "Center")
        self.game_title_text = Label(self.carousel.objects[self.carousel.current_object].title,
                                 self.carousel.objects[self.carousel.current_object].text_color,
                                 512, 650,
                                 None,
                                 self.carousel.objects[self.carousel.current_object].font_face)
        self.player_text = Label(self.carousel.objects[self.carousel.current_object].players,
                                 (255, 255, 255),
                                 512, 700,
                                 None,
                                 self.BODY_FONT)

        self.drawable_objects.append(self.game_poster)
        self.drawable_objects.append(self.game_title_text)
        self.drawable_objects.append(self.player_text)

        load_music('arcade_machine/resources/audio/Main_Menu/Theme.mp3')
        play_music()  # loop indefinitely

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_j:
                self.carousel.decrement()
                self.update_colors_list()
                self.update_game_title()
            elif event.key == K_d or event.key == K_l:
                self.carousel.increment()
                self.update_colors_list()
                self.update_game_title()
            elif event.key == K_1 or event.key == K_9:
                stop_music()
                event = Event(CHANGE_GAME, {"game": self.carousel.objects[self.carousel.current_object].title})
                pygame_post_event(event)
            elif event.key == K_m:
                stop_music()
                event = Event(CHANGE_GAME, {"game": "Settings"})
                pygame_post_event(event)
            elif event.key == K_ESCAPE: #TODO: Remove escape functionality
                pygame_quit()
                exit()

    def update(self):
        if self.animation_timer <= self.animation_steps: # Control the bg color change
            self.background = self.color_list[self.animation_timer]
            self.animation_timer += 1

    def update_game_title(self):
        self.game_poster.change_image(self.carousel.objects[self.carousel.current_object].poster)
        self.game_title_text.redraw_label(text=self.carousel.objects[self.carousel.current_object].title,
                                          color=self.carousel.objects[self.carousel.current_object].text_color,
                                          font=self.carousel.objects[self.carousel.current_object].font_face)
        self.player_text.redraw_label(text=self.carousel.objects[self.carousel.current_object].players)

    def update_colors_list(self):
        self.color_list = get_blended_colors_list(self.background, self.carousel.objects[self.carousel.current_object].bg_color, self.animation_steps)
        self.animation_timer = 0
