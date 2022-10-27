import math
import random, os, string

from pygame.transform import rotate, scale
from pygame.sprite import Sprite, Group
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame import Surface
from arcade_machine.events import CHANGE_GAME
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.ellipse import Ellipse
from arcade_machine.font_manager import font_manager
from arcade_machine.high_score_manager import high_score_manager
from arcade_machine.sprites.image_sprite import ImageSprite
from arcade_machine.images.asteroid_universe_images import *
from pygame.mixer import Sound
from arcade_machine.components.carousel_menu import CarouselMenu

class Starcraft():
    def __init__(self):
        self.imagesprite = ImageSprite(starcraft, 512, 700, 'Center')
        self.lefty = Booster()
        self.righty = Booster()
        self.degrees = 0

    def update(self):
        self.degrees %= 360
        if self.degrees < 0:
            self.degrees *= -1
        self.imagesprite.rotate_image(new_angle=self.degrees)
        new_x = (316 * math.cos(math.radians((self.degrees - 90))) + 512)
        new_y = (316 * math.sin(math.radians((self.degrees - 90))) + 384)
        self.imagesprite.move_image(set_x=new_x, set_y=new_y)

class Booster():
    def __init__(self):
        self.particles = []

class BackgroundStar():
    def __init__(self):
        self.x = random.randint(10, 1014)
        self.y = random.randint(10, 758)
        self.count = 1
        self.size = random.randint(1, 4)
        self.intensity = int((random.randint(5, 10) * 255) / 10)
        self.color = (self.intensity, self.intensity, self.intensity)
        self.object = Ellipse(x_pos=self.x, y_pos=self.y, color=self.color, width=self.size, height=self.size)
        self.path = random.randint(0, 359)
        self.center_dist = math.sqrt(pow(abs(self.x - 512), 2) + pow(abs(self.y - 368), 2))
        self.velocity_x = round(random.uniform(-4, 4), 2)
        self.velocity_y = round(random.uniform(-4, 4), 2)
        self.check_velocity()
        self.velocity = 1

    def birth(self):
        self.size = random.randint(1, 4)
        self.intensity = int((random.randint(5, 10) * 255) / 10)
        self.color = (self.intensity, self.intensity, self.intensity)
        self.object.change_ellipse_dimension(new_width=self.size, new_height=self.size)
        self.object.change_ellipse_color(new_color=self.color)
        self.object.change_ellipse_position(new_x=512, new_y=368, new_anchor='Center')
        self.path = round(random.uniform(0,359), 2)
        self.velocity_x = round(random.uniform(-4,4), 2)
        self.velocity_y = round(random.uniform(-4,4), 2)
        self.check_velocity()
        self.count = 1

    def check_velocity(self):
        if self.velocity_x == 0:
            self.velocity_x = round(random.uniform(-4, 4), 2)
            self.check_velocity()
        elif self.velocity_y == 0:
            self.velocity_y = round(random.uniform(-4, 4), 2)
            self.check_velocity()
        else:
            return

    def update(self):
        self.count += 1
        self.center_dist = math.sqrt(pow(abs(self.object.sprite.rect.x - 512), 2) + pow(abs(self.object.sprite.rect.y - 368), 2))
        self.velocity = pow(0.002 * self.center_dist, 2) + 1
        self.object.change_ellipse_position(new_x=(int(self.velocity_x * self.count * self.velocity) + 512),
                                            new_y=(int(self.velocity_y * self.count * self.velocity) + 368),
                                            new_anchor='Center')

        if self.object.sprite.rect.x < -4 or self.object.sprite.rect.x > 1028:
            self.birth()
        if self.object.sprite.rect.y < -4 or self.object.sprite.rect.y > 772:
            self.birth()

class AsteroidUniverse(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (1, 6, 12)
        self.starcraft = Starcraft()


        self.bgstars = []
        for i in range(0, 230):
            star = BackgroundStar()
            self.bgstars.append(star)
        self.star_group = Group()
        for light in self.bgstars:
            self.star_group.add(light.object.sprite)
        self.drawable_objects.append(self.star_group)
        self.drawable_objects.append(self.starcraft.imagesprite)

    def handle_event(self, event):
        if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
            event = Event(CHANGE_GAME, {"game": "MainMenu"})
            pygame_post_event(event)
            return
        if event == 'P1_E_DOWN' or event == 'P2_E_DOWN':
            self.starcraft.degrees -= 5
            print(self.starcraft.degrees, (316 * math.cos(math.radians((self.starcraft.degrees - 90))) + 512), (316 * math.sin(math.radians((self.starcraft.degrees - 90))) + 384))
        if event == 'P1_W_DOWN' or event == 'P2_W_DOWN':
            self.starcraft.degrees += 5
            print(self.starcraft.degrees, self.starcraft.imagesprite.sprite.rect.x,
                  self.starcraft.imagesprite.sprite.rect.y)


    def update(self):
        for i in self.bgstars:
            i.update()
        self.starcraft.update()