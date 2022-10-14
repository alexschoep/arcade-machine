import random, os

import pygame.transform
from pygame import BLEND_RGBA_MULT, BLEND_RGBA_MIN, BLEND_RGBA_MAX, BLENDMODE_MOD
from pygame.sprite import Sprite, Group
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame import Surface, image
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.ellipse import Ellipse
from arcade_machine.font_manager import font_manager
from arcade_machine.high_score_manager import high_score_manager
from arcade_machine.sprites.image_sprite import ImageSprite
from arcade_machine.components.parallax import Parallax
from arcade_machine.images.mars_lander_images import *
from pygame.mixer import Sound

from random import randint

class Planet(Sprite):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.index = 0
        self.planet_animation = []
        for file_name in os.listdir(r"arcade_machine/resources/images/mars_lander/planet_animation/titan"):
            img = Image((r"arcade_machine/resources/images/mars_lander/planet_animation/titan" + os.sep + file_name))
            sp_img = ImageSprite(img, 732, 360, "Center")
            sp_img.scale_image(new_dim=(150, 150))
            self.planet_animation.append(sp_img)
        self.image = self.planet_animation[self.index]

    def update(self):
        self.counter += 1
        if self.counter % 3 == 0:
            self.index += 1
        self.counter %= 30
        self.index %= 50
        self.image = self.planet_animation[self.index]

class BackroundStar(Sprite):
    def __init__(self):
        super().__init__()
        self.size = random.randint(1, 4)
        self.intensity = int((random.randint(5, 10) * 255) / 10)
        self.image = Surface((self.size, self.size))
        self.image.fill((self.intensity, self.intensity, self.intensity))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(4, 1020)

    def update(self):
        pass 


class MarsLander(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (255 , 255, 255)
        self.game_state = 'START'
        self.game_mode = "MARS" # MOON, NEPTUNE, TITAN, DEEPSPACE
        self.num_stars = 100

        # --- INDICATORS ---
        self.start_menu_option = 0


        self.title_font = font_manager.get_font('lemon_milk', 108)
        self.header_font = font_manager.get_font('lemon_milk', 72)
        self.large_font = font_manager.get_font('lemon_milk', 36)
        self.body_font = font_manager.get_font('lemon_milk', 24)
        self.small_font = font_manager.get_font('lemon_milk', 12)

        self.button_sound = Sound('arcade_machine/resources/audio/Mars Lander/button.wav')
        self.button_sound.set_volume(pygame.mixer_music.get_volume())


        # --- START MENU OBJECTS ---
        self.game_title = Label('MARS LANDER', (242, 101, 34), 512, 110, self.title_font)
        self.divider = Rectangle(color=(200, 200, 200), x_pos=0, y_pos=200, width=1024, height=6, line_weight=0,
                                 bevel=0, alpha=255, anchor="TopLeft")
        self.start_label = Label('START', (0, 0, 0), 512, 320, self.header_font)
        self.controls_label = Label('CONTROLS', (200, 200, 200), 512, 420, self.header_font)
        self.abort_label = Label('ABORT', (200, 200, 200), 512, 520, self.header_font)

        # --- CONTROLS SCREEN OBJECTS ---

        # --- TRAJECTORY SCREEN OBJECTS ---

        # --- GAME PLAY OBJECTS ---

        # --- GAME OVER OBJECTS ---

        # --- HIGH SCORE OBJECTS ---

        # --- SCORE OBJECTS ---


        #self.game_subtitle = Label('Artemis Missons', (100, 100, 100), 512, 230, self.large_font, anchor='MidLeft')

        self.gray_rect = Rectangle(width=824, height=380, x_pos=512, y_pos=360, color=(200, 200, 200), bevel=22,
                                 anchor='Center')
        self.black_rect = Rectangle(width=360, height=360, x_pos=732, y_pos=360, color=(0, 0, 0), bevel=18,
                                 anchor='Center')

        self.dest_label = Label('DESTINATION:', (100, 100, 100), 120, 220, self.large_font, anchor='BottomLeft')
        self.game_mode_label = Label(self.game_mode, (0, 0, 0), 120, 280, self.header_font, anchor='BottomLeft')
        self.gravity_label = Label('GRAVITY:', (100, 100, 100), 120, 340, self.large_font, anchor='BottomLeft')
        self.planet_gravity_label = Label('0.6G', (0, 0, 0), 120, 380, self.large_font, anchor='BottomLeft')
        self.data_label = Label('DATA:', (100, 100, 100), 120, 450, self.large_font, anchor='BottomLeft')
        self.anomalies_label = Label('No Anomalies', (0, 0, 0), 120, 490, self.large_font, anchor='BottomLeft')



        #self.star_cluster = Group()
        #self.drawable_objects.append(self.star_cluster)
        #for i in range(0, self.num_stars):
        #    star = BackroundStar()
        #    self.star_cluster.add(star)

        self.mars_planet = Planet()
        self.planet_group = Group()
        self.planet_group.add(self.mars_planet.image)

        #self.planet = ImageSprite(mars_planet, 500, 500, "Center")
        #self.ellipse = Ellipse(width=250, height=250, x_pos=500, y_pos=100, alpha=255, color=(255,255,255), anchor='TopLeft')
        #self.ellipse.sprite.image.blit(self.planet.sprite.image, (0, 0), None, BLEND_RGBA_MULT)
        #self.step = 0
        #masked_result.blit(mask_surface, (0, 0), None, pygame.BLEND_RGBA_MULT)


        #self.parallax = Parallax(self.planet)
        #self.parallax.scroll(5, 5)

        self.start_screen_view()



    def handle_event(self, event):
        if self.game_state == 'START':
            if event == 'P1_N_DOWN' or event == 'P2_N_DOWN':
                self.start_menu_option -= 1
                self.button_sound.play()
            if event == 'P1_S_DOWN' or event == 'P2_S_DOWN':
                self.start_menu_option += 1
                self.button_sound.play()
            if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
                if self.start_menu_option == 0:
                    self.game_state = 'TRAJ'
                    self.trajectory_screen_view()
                elif self.start_menu_option == 1:
                    self.controls_screen_view()
                elif self.start_menu_option == 2:
                    event = Event(CHANGE_GAME, {"game": "MainMenu"})
                    pygame_post_event(event)
                    return
                self.button_sound.play()


    def update(self):
        if self.game_state == 'START':
            self.start_screen_update()
        elif self.game_state == 'TRAJ':
            self.trajectory_screen_update()

    def start_screen_view(self):
        self.drawable_objects.clear()
        self.drawable_objects.append(self.game_title)
        self.drawable_objects.append(self.divider)
        self.drawable_objects.append(self.start_label)
        self.drawable_objects.append(self.controls_label)
        self.drawable_objects.append(self.abort_label)


    def start_screen_update(self):
        if self.start_menu_option < 0:
            self.start_menu_option = 0
        elif self.start_menu_option > 2:
            self.start_menu_option = 2

        if self.start_menu_option == 0:
            self.start_label.redraw_label(color=(0, 0, 0))
            self.controls_label.redraw_label(color=(200, 200, 200))
        elif self.start_menu_option == 1:
            self.start_label.redraw_label(color=(200, 200, 200))
            self.controls_label.redraw_label(color=(0, 0, 0))
            self.abort_label.redraw_label(color=(200, 200, 200))
        elif self.start_menu_option == 2:
            self.controls_label.redraw_label(color=(200, 200, 200))
            self.abort_label.redraw_label(color=(0, 0, 0))

    def controls_screen_view(self):
        pass

    def controls_screen_update(self):
        pass


    def trajectory_screen_view(self):
        self.drawable_objects.clear()
        # self.drawable_objects.append(self.game_subtitle)
        self.drawable_objects.append(self.gray_rect)
        self.drawable_objects.append(self.black_rect)

        self.drawable_objects.append(self.dest_label)
        self.drawable_objects.append(self.game_mode_label)
        self.drawable_objects.append(self.gravity_label)
        self.drawable_objects.append(self.planet_gravity_label)
        self.drawable_objects.append(self.data_label)
        self.drawable_objects.append(self.anomalies_label)

        self.drawable_objects.append(self.planet_group)

    def trajectory_screen_update(self):
        self.mars_planet.update()
        self.planet_group.empty()
        self.planet_group.add((self.mars_planet.image))