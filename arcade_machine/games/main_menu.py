import pygame.sprite
from pygame import KEYDOWN, K_a, K_d, K_j, K_l, K_ESCAPE, K_m
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame import quit as pygame_quit
from pygame import font

from arcade_machine.Controller.music_player import load_music, play_music
from arcade_machine.components.game_title import Title
from arcade_machine.utility.color_blender import get_blended_colors_list

from arcade_machine.events import CHANGE_GAME
from arcade_machine.sprites.label import Label
from arcade_machine.games.game import Game


class MainMenu(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.animation_timer = 0 # Used for bg coloring
        self.button_flag = True # Flag if a button is pressed
        self.index = 0 # Index for games carousel
        self.background = (0, 0, 0)
        self.color_list = [] # Used for bg coloring

        load_music('arcade_machine/resources/audio/Main_Menu/Theme.mp3')
        play_music(-1) # loop indefinitely

        self.TITLE_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 48)
        self.BODY_FONT = font.Font('arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf', 24)
        self.menu_title = Label('Arcade Machine', (255, 255, 255), 512, 60, None, self.TITLE_FONT)
        self.drawable_objects.append(self.menu_title)

        self.game_titles = []
        self.create_game_titles() # Create a list for all the games & display attributes
        self.poster = None
        self.poster_group = pygame.sprite.Group()

        self.player_text = Label('Players', (255, 255, 255), 512, 700, None, self.BODY_FONT)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_j:
                self.index -= 1
                self.button_flag = True
            elif event.key == K_d or event.key == K_l:
                self.index += 1
                self.button_flag = True
            elif event.key == K_m:
                event = Event(CHANGE_GAME, {"game": "Settings"})
                pygame_post_event(event)
            elif event.key == K_ESCAPE: #TODO: Remove escape functionality
                pygame_quit()
                exit()
    def create_game_titles(self):
        #For each game available, create a title for display
        asteroid = Title("Asteroid Universe", "arcade_machine/resources/images/Main_Menu/Asteroid.png", (84, 139, 161),
                     "arcade_machine/resources/fonts/Asteroid Universe/RACING HARD.ttf", (16, 48, 61), 1)
        self.game_titles.append(asteroid)
        pong = Title("PONG", "arcade_machine/resources/images/Main_Menu/No Image.png", (200, 200, 200),
                     "arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf", (0, 0, 0), 0)
        self.game_titles.append(pong)
        snake = Title("Snake", "arcade_machine/resources/images/Main_Menu/No Image.png", (62, 59, 156),
                      "arcade_machine/resources/fonts/Snake/04B_30__.ttf", (121, 120, 156), 1)
        self.game_titles.append(snake)
        marslander = Title("Mars Lander", "arcade_machine/resources/images/Main_Menu/Mars Lander.png", (241, 219, 205),
                      "arcade_machine/resources/fonts/Mars Lander/LemonMilk.otf", (200, 59, 0), 1)
        self.game_titles.append(marslander)

    def update(self):
        if self.button_flag:
            if self.index > len(self.game_titles) - 1: # Loop the carousel when at the end of the list
                self.index = 0
            elif self.index < 0:
                self.index = len(self.game_titles) - 1

            self.color_list = get_blended_colors_list(self.background, self.game_titles[self.index].bg_color, 8)
            self.button_flag = False
            self.animation_timer = 0

            self.poster_group.empty()
            self.poster = self.game_titles[self.index].poster
            self.poster_group.add(self.poster)

            if self.game_titles[self.index].players == 0: # Set the no. players text
                text = "1 and 2 Players"
            elif self.game_titles[self.index].players == 1:
                text = "Single Player"
            elif self.game_titles[self.index].players == 2:
                text = "Two Players"
            self.player_text = Label(text, (255, 255, 255), 512, 720, None, self.BODY_FONT)

        if self.animation_timer <= 8: # Control the bg color change
            self.background = self.color_list[self.animation_timer]
            self.animation_timer += 1

        self.drawable_objects.clear() # Clear the objects, so they will not layer and prepare to redraw

        self.drawable_objects.append(self.menu_title)
        self.drawable_objects.append(self.player_text)
        self.drawable_objects.append(self.poster_group)

        self.game_title = Label(self.game_titles[self.index].title,
                                self.game_titles[self.index].text_color,
                                512, 650,
                                None,
                                self.game_titles[self.index].font_face)
        self.drawable_objects.append((self.game_title))

