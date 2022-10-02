import random

from pygame import KEYDOWN, KEYUP, K_m, K_p, K_1, K_8, K_w, K_a, K_s, K_d, K_i, K_j, K_k, K_l
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame import Surface, image
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.label import Label
from arcade_machine.font_manager import font_manager
from arcade_machine.controllers import high_score_manager
from arcade_machine.sprites.image_sprite import ImageSprite
from arcade_machine.images.mars_lander_images import *




from random import randint

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
        self.background = (0, 0, 0)
        self.game_state = 'START'
        self.game_mode = "ARTEMIS" # MOON, NEPTUNE, TITAN, DEEPSPACE
        self.num_stars = 100

        self.header_font = font_manager.get_font('lemon_milk', 72)
        self.large_font = font_manager.get_font('lemon_milk', 48)
        self.body_font = font_manager.get_font('lemon_milk', 24)
        self.small_font = font_manager.get_font('lemon_milk', 12)

        self.game_title = Label('MARS LANDER', (0, 0, 0), 512, 180, self.header_font)
        self.game_subtitle = Label('Artemis Missons', (100, 100, 100), 512, 230, self.large_font)

        self.star_cluster = Group()
        self.drawable_objects.append(self.star_cluster)
        for i in range(0, self.num_stars):
            star = BackroundStar()
            self.star_cluster.add(star)

        self.planet = ImageSprite(mars_planet, 512, 360, "Center")

        self.start_screen_view()



    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_m:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
            if event.key == K_1 or event.key == K_8:
                pass

        if event.type == KEYUP:
            if event.key == K_1 or event.key == K_8:
                pass

    def update(self):
        self.star_cluster.update()
        pass

    def start_screen_view(self):
        self.drawable_objects.clear()
        self.title_rectangle = Rectangle(color=(255, 255, 255),
                                     x_pos=0,
                                     y_pos=0,
                                     width=1024,
                                     height=300,
                                     line_weight=0,
                                     bevel=0,
                                     alpha=255,
                                     anchor="TopLeft")
        self.drawable_objects.append(self.title_rectangle)
        self.drawable_objects.append(self.star_cluster)
        self.drawable_objects.append(self.game_title)
        self.drawable_objects.append(self.game_subtitle)

    def start_screen_update(self):
        pass
