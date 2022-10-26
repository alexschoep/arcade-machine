import math
import random, os, string

import pygame.transform
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
from arcade_machine.images.mars_lander_images import *
from pygame.mixer import Sound
from arcade_machine.components.carousel_menu import CarouselMenu

mars_level_data = [
    [(100, 100), (296, 595), (680, 609), mars_level_0], # Start coord, min land coord, max land coord
    [(100, 100), (764, 583), (856, 595), mars_level_1],
    [(100, 100), (704, 427), (748, 439), mars_level_2],
    [(800, 100), (296, 595), (400, 609), mars_level_3],
    [(80, 80), (440, 619), (464, 631), mars_level_4],
    [(750, 70), (212, 595), (236, 609), mars_level_5],
    [(80, 80), (524, 619), (604, 631), mars_level_6],
    [(820, 400), (444, 211), (468, 223), mars_level_7],
    [(870, 80), (464, 607), (472, 621), mars_level_8],
    [(870, 80), (212, 595), (268, 609), mars_level_9],
    [(40, 80), (704, 607), (748, 621), mars_level_10],
    [(820, 80), (164, 583), (280, 597), mars_level_11],
    [(820, 80), (428, 619), (472, 631), mars_level_12],
    [(480, 80), (500, 619), (580, 631), mars_level_13],
    [(800, 100), (368, 619), (436, 631), mars_level_14],
    [(100, 100), (824, 595), (868, 609), mars_level_15],
    [(400, 100), (824, 583), (856, 597), mars_level_16],
    [(600, 70), (464, 619), (616, 631), mars_level_17],
    [(80, 80), (776, 403), (820, 415), mars_level_18],
    [(150, 100), (596, 619), (640, 631), mars_level_19]
]

class Planet(Sprite):
    def __init__(self, game_mode):
        super().__init__()

        self.counter = 0
        self.index = 0
        self.planet_animation = []
        self.planet_path = r"arcade_machine/resources/images/mars_lander/planet_animation/" + game_mode
        for file_name in sorted(os.listdir(self.planet_path)):
            img = Image((self.planet_path + os.sep + file_name))
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
        self.rect.y = random.randrange(4, 764)
        self.rect.x = random.randrange(0, 1023)
        self.count = 0

    def update(self):
        if self.rect.x > 1024:
            self.rect.x = -2
            self.rect.y = random.randrange(4, 764)
        if self.count % 3 == 0:
            self.count = 0
            self.rect.x += (4 * (5 - self.size))
        self.count += 1

class Lander():
    def __init__(self):
        self.lander = ImageSprite(lander, 100, 100, 'TopLeft')
        self.x_vel = 0
        self.y_vel = 0
        self.fuel = 700
        self.crash = False
        self.collision_cooldown = 0
        self.thrust_x = 0
        self.thrust_y = 0
        self.touchdown = False
        self.deadstick = False
        self.los = False

    def update(self):
        if self.crash == True:
            self.lander.change_image(lander_crash)
            self.x_vel = 0
            self.y_vel = 0
            self.collision_cooldown += 1
            return
        if self.touchdown == True:
            self.x_vel = 0
            self.y_vel = 0
            self.collision_cooldown += 1
            return
        if self.los == True or self.fuel == 0:
            self.deadstick = True

        if self.deadstick == False:
            self.x_vel += self.thrust_x
            self.y_vel += self.thrust_y
            if self.thrust_x != 0:
                self.fuel -= 7
            if self.thrust_y != 0:
                self.fuel -= 7

        if self.fuel < 0:
            self.fuel = 0

        if self.lander.sprite.rect.x < -64 or\
                self.lander.sprite.rect.x > 1024 or\
                self.lander.sprite.rect.y < -64 or\
                self.lander.sprite.rect.y > 768:
            self.crash = True

        self.y_vel += 1
        if self.y_vel > 8:
            self.y_vel = 8
        if self.x_vel > 12:
            self.x_vel = 12
        elif self.x_vel < -12:
            self.x_vel = -12
        self.lander.move_image(step_x=self.x_vel, step_y=self.y_vel)

    def set_level(self, x_pos, y_pos):
        self.lander.change_image(lander)
        self.lander.move_image(set_x=x_pos, set_y=y_pos)
        self.x_vel = 0
        self.y_vel = 0
        self.fuel = 700
        self.crash = False
        self.thrust_x = 0
        self.thrust_y = 0
        self.touchdown = False
        self.deadstick = False
        self.los = False
        self.collision_cooldown = 0

class PlanetSurface():
    def __init__(self):
        self.terrain = ImageSprite(mars_level_0, 512, 697, 'MidBottom')
        self.terrain.scale_image(new_dim=(960, 576))

    def new_level(self, level):
        self.terrain.change_image(mars_level_data[level][3])
        self.terrain.scale_image(new_dim=(960, 576))

class FuelBar():
    def __init__(self, length, height, color, x, y):
        self.length = length
        self.height = height
        self.color = color
        self.bar = Rectangle(height=height, width=length, color=color, x_pos=x, y_pos=y, anchor='TopLeft')

    def update(self, length):
        if length <= 0:
            return
        self.bar.change_rectangle_dimension(length, self.height)
        if length <= (0.15 * self.length):
            self.bar.change_rectangle_color((160, 20, 4))
        elif length <= (0.4 * self.length):
            self.bar.change_rectangle_color((170, 170, 4))
    def reset(self):
        self.bar.change_rectangle_dimension(self.length, self.height)
        self.bar.change_rectangle_color(self.color)

class Thruster():
    def __init__(self):
        self.particles = []

    def add_thrust(self, x_pos, y_pos, offset_x, offset_y, direction):
        particle = Ellipse(x_pos=(x_pos + offset_x), y_pos=(y_pos + offset_y), color=(255, 255, 255), width=5, height=5, anchor='TopLeft')
        scatter = round(random.uniform(-0.5,0.5), 2)
        blast = [particle, offset_x, offset_y, direction, 24, scatter]
        self.particles.append(blast)

    def update(self, nozzle_x, nozzle_y):
        for flame in self.particles:
            flame[4] -= 3
            if flame[4] <= 0:
                self.particles.remove(flame)
            size = int(flame[4] / 3)
            flame[0].change_ellipse_dimension(size, size)
            blue_val = int(((1.2 * flame[4]) - 15)**2)
            flame[0].change_ellipse_color((255,
                                           (10 * flame[4]),
                                           blue_val))
            if flame[3] == 'South':
                flame[0].change_ellipse_position(((nozzle_x + flame[1]) + int((24 - flame[4]) * flame[5])),
                                                 ((nozzle_y + flame[2]) + (24 - flame[4])),
                                                 'TopLeft')
            elif flame[3] == 'West':
                flame[0].change_ellipse_position(((nozzle_x + flame[1]) - (24 - flame[4])),
                                                 ((nozzle_y + flame[2]) + int((24 - flame[4]) * flame[5])),
                                                 'TopLeft')
            elif flame[3] == 'East':
                flame[0].change_ellipse_position(((nozzle_x + flame[1]) + (24 - flame[4])),
                                                 ((nozzle_y + flame[2]) + int((24 - flame[4]) * flame[5])),
                                                 'TopLeft')


class MarsLander(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (255 , 255, 255)
        self.game_state = 'START'
        self.game_mode = "mars" # MOON, NEPTUNE, TITAN, DEEPSPACE
        self.level = 0
        self.num_stars = 35
        self.los = False
        self.score = 0
        self.initials_position = 0

        # --- INDICATORS ---
        self.start_menu_option = 0

        self.title_font = font_manager.get_font('lemon_milk', 108)
        self.header_font = font_manager.get_font('lemon_milk', 72)
        self.xlarge_font = font_manager.get_font('lemon_milk', 48)
        self.large_font = font_manager.get_font('lemon_milk', 36)
        self.body_font = font_manager.get_font('lemon_milk', 24)
        self.small_font = font_manager.get_font('lemon_milk', 12)

        self.button_sound = Sound('arcade_machine/resources/audio/Mars Lander/button.wav')
        self.button_sound.set_volume(pygame.mixer_music.get_volume())
        self.crash_sound = Sound('arcade_machine/resources/audio/Mars Lander/crashed.wav')
        self.crash_sound.set_volume(pygame.mixer_music.get_volume())
        self.thrust_sound = Sound('arcade_machine/resources/audio/Mars Lander/Thrusting.wav')
        self.thrust_sound.set_volume(pygame.mixer_music.get_volume())

        # --- START MENU OBJECTS ---
        self.game_title = Label('MARS LANDER', (242, 101, 34), 512, 110, self.title_font)
        self.divider = Rectangle(color=(200, 200, 200), x_pos=0, y_pos=200, width=1024, height=6, line_weight=0,
                                 bevel=0, alpha=255, anchor="TopLeft")
        self.start_label = Label('START', (0, 0, 0), 512, 320, self.header_font)
        self.controls_label = Label('CONTROLS', (200, 200, 200), 512, 420, self.header_font)
        self.abort_label = Label('ABORT', (200, 200, 200), 512, 520, self.header_font)

        # --- CONTROLS SCREEN OBJECTS ---
        self.controls_title = Label('CONTROLS', (242, 101, 34), 512, 110, self.title_font)
        self.joystick_controls1 = Label("THE JOYSTICK FIRES", (200, 200, 200), 512, 320, self.xlarge_font)
        self.joystick_controls2 = Label("THE LANDER'S THRUSTERS", (200, 200, 200), 512, 370, self.xlarge_font)
        self.button_controls1 = Label("THE BUTTONS OPERATE", (200, 200, 200), 512, 520, self.xlarge_font)
        self.button_controls2 = Label("THE SPECIAL FUNCTIONS", (200, 200, 200), 512, 570, self.xlarge_font)
        self.back_label = Label("PRESS 'A' TO RETURN TO THE MENU", (0, 0, 0), 512, 720, self.large_font)

        # --- TRAJECTORY SCREEN OBJECTS ---
        self.dest_label = Label('DESTINATION:', (100, 100, 100), 120, 210, self.large_font, anchor='BottomLeft')
        self.game_mode_label = Label(self.game_mode, (255, 255, 255), 120, 280, self.header_font, anchor='BottomLeft')
        self.gravity_label = Label('GRAVITY:', (100, 100, 100), 120, 340, self.large_font, anchor='BottomLeft')
        self.planet_gravity_label = Label('0.38G', (255, 255, 255), 120, 380, self.large_font, anchor='BottomLeft')
        self.data_label = Label('DATA:', (100, 100, 100), 120, 450, self.large_font, anchor='BottomLeft')
        self.anomalies_label = Label('No Anomalies', (255, 255, 255), 120, 490, self.large_font, anchor='BottomLeft')
        self.launch_label = Label('LAUNCH', (242, 101, 34), 512, 680, self.header_font, anchor='Center')
        self.mars_planet = Planet(self.game_mode)
        self.planet_group = Group()
        self.planet_group.add(self.mars_planet.image)
        self.star_cluster = Group()
        for i in range(0, self.num_stars):
            star = BackroundStar()
            self.star_cluster.add(star)

        # --- GAME PLAY OBJECTS ---
        self.fuel_label = Label('FUEL', (255, 255, 255), 30, 20, self.body_font, anchor='TopLeft')
        self.score_label = Label('SCORE:', (255, 255, 255), 824, 20, self.body_font, anchor='TopLeft')
        self.score_value_label = Label('000', (255, 255, 255), 994, 20, self.body_font, anchor='TopRight')
        self.fuel = FuelBar(700, 12, (20, 200, 92), 100, 26)
        self.game_area = Rectangle(color=(255, 255, 255), x_pos=512, y_pos=60, line_weight=3, anchor='MidTop', width=966, height=640)
        self.los_label = Label('L. O. S.', (255, 255, 255), 512, 348, self.header_font, anchor='Center')
        self.los_label2 = Label('Loss of Signal', (255, 255, 255), 512, 400, self.body_font, anchor='Center')
        self.los_rect = Rectangle(color=(255, 255, 255), x_pos=512, y_pos=260, line_weight=5, bevel=25, anchor='MidTop', width=400, height=200)
        self.los_group = Group()
        self.los_group.add(self.los_label)
        self.los_group.add(self.los_label2)
        self.los_group.add(self.los_rect)
        self.thrust = Thruster()

        self.spacecraft = Lander()
        self.planet_surface = PlanetSurface()
        self.thrust_group = Group()

        # --- GAME OVER OBJECTS ---

        # --- HIGH SCORE OBJECTS ---
        self.initials_title = Label('ENTER INITIALS', (242, 101, 34), 512, 110, self.title_font)
        self.initials_letter0 = Label('A', (200, 200, 200), 412, 420, self.title_font)
        self.initials_letter1 = Label('A', (200, 200, 200), 512, 420, self.title_font)
        self.initials_letter2 = Label('A', (200, 200, 200), 612, 420, self.title_font)
        self.initials_continue = Label("PRESS 'A' TO CONTINUE", (0, 0, 0), 512, 690, self.xlarge_font)
        self.carousel_initials_0 = CarouselMenu(list(string.ascii_uppercase))
        self.carousel_initials_1 = CarouselMenu(list(string.ascii_uppercase))
        self.carousel_initials_2 = CarouselMenu(list(string.ascii_uppercase))

        # --- SCORE OBJECTS ---
        self.highscores_title = Label('HIGHSCORES', (242, 101, 34), 512, 110, self.title_font)
        self.top_high_score_label = Label("Person", (200, 200, 200), 512, 300, self.header_font)
        self.mid_high_score_label = Label("Person", (200, 200, 200), 512, 400, self.header_font)
        self.low_high_score_label = Label("Person", (200, 200, 200), 512, 500, self.header_font)

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
                    self.game_state = 'CONT'
                    self.controls_screen_view()
                elif self.start_menu_option == 2:
                    event = Event(CHANGE_GAME, {"game": "MainMenu"})
                    pygame_post_event(event)
                    return
                self.button_sound.play()
        elif self.game_state == 'CONT':
            if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
                self.button_sound.play()
                self.game_state = 'START'
                self.start_screen_view()
        elif self.game_state == 'TRAJ':
            if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
                self.button_sound.play()
                self.game_state = 'GAME'
                self.game_screen_view()
            if event == 'MENU_DOWN':
                self.game_state = 'START'
                self.start_screen_view()
        elif self.game_state == 'GAME':
            if event == 'P1_N_DOWN' or event == 'P2_N_DOWN':
                self.spacecraft.thrust_y = -2
                self.thrust_sound.play()
            if event == 'P1_NS_UP' or event == 'P2_NS_UP':
                self.spacecraft.thrust_y = 0
            if event == 'P1_E_DOWN' or event == 'P2_E_DOWN':
                self.spacecraft.thrust_x = 2
                self.thrust_sound.play()
            if event == 'P1_W_DOWN' or event == 'P2_W_DOWN':
                self.spacecraft.thrust_x = -2
                self.thrust_sound.play()
            if event == 'P1_EW_UP' or event == 'P2_EW_UP':
                self.spacecraft.thrust_x = 0

        elif self.game_state == 'HIGH':
            if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
                self.button_sound.play()
                self.set_score()
                self.game_state = 'SCORE'
                self.view_highscores_view()
            if event == 'P1_W_DOWN' or event == 'P2_W_DOWN':
                self.initials_position -= 1
            if event == 'P1_E_DOWN' or event == 'P2_E_DOWN':
                self.initials_position += 1
            if event == 'P1_N_DOWN' or event == 'P2_N_DOWN':
                self.change_letter('UP')
            if event == 'P1_S_DOWN' or event == 'P2_S_DOWN':
                self.change_letter('DOWN')

        elif self.game_state == 'SCORE':
            if event == 'P1_A_DOWN' or event == 'P2_A_DOWN':
                self.button_sound.play()
                self.reset_game()
                self.game_state = 'START'
                self.start_screen_view()
        elif self.game_state == 'OVER':
            self.button_sound.play()
            if self.check_scores():
                self.game_state = 'HIGH'
                self.high_score_entry_view()
            else:
                self.game_state = 'SCORE'
                self.view_highscores_view()

    def update(self):
        if self.game_state == 'GAME':
            self.game_screen_update()
        elif self.game_state == 'START':
            self.start_screen_update()
        elif self.game_state == 'TRAJ':
            self.trajectory_screen_update()
        elif self.game_state == 'HIGH':
            self.high_score_entry_update()
        elif self.game_state == 'SCORE':
            self.view_highscores_update()
        elif self.game_state == 'CONT':
            self.controls_screen_update()

    def start_screen_view(self):
        self.background = (255, 255, 255)
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
        self.drawable_objects.clear()
        self.drawable_objects.append(self.controls_title)
        self.drawable_objects.append(self.divider)
        self.drawable_objects.append(self.joystick_controls1)
        self.drawable_objects.append(self.joystick_controls2)
        self.drawable_objects.append(self.button_controls1)
        self.drawable_objects.append(self.button_controls2)
        self.drawable_objects.append(self.back_label)

    def controls_screen_update(self):
        pass


    def trajectory_screen_view(self):
        self.background = (0, 0, 0)
        self.drawable_objects.clear()
        self.drawable_objects.append(self.star_cluster)

        self.drawable_objects.append(self.dest_label)
        self.drawable_objects.append(self.game_mode_label)
        self.drawable_objects.append(self.gravity_label)
        self.drawable_objects.append(self.planet_gravity_label)
        self.drawable_objects.append(self.data_label)
        self.drawable_objects.append(self.anomalies_label)
        self.drawable_objects.append(self.launch_label)

        self.drawable_objects.append(self.planet_group)

    def trajectory_screen_update(self):
        self.star_cluster.update()
        self.mars_planet.update()
        self.planet_group.empty()
        self.planet_group.add((self.mars_planet.image))

    def game_screen_view(self):
        self.drawable_objects.clear()
        if self.game_mode == 'mars':
            self.drawable_objects.append(self.fuel_label)
            self.drawable_objects.append(self.score_label)
            self.drawable_objects.append(self.score_value_label)
            self.drawable_objects.append(self.fuel.bar)
            self.drawable_objects.append(self.game_area)


        self.setup_level()
        self.drawable_objects.append(self.thrust_group)
        self.drawable_objects.append(self.planet_surface.terrain)
        self.drawable_objects.append(self.spacecraft.lander)
        self.drawable_objects.append(self.los_group)

    def game_screen_update(self):
        self.landing_collision()
        self.fuel.update(self.spacecraft.fuel)
        self.spacecraft.update()
        if self.game_mode == 'titan':
            pass

        if self.spacecraft.touchdown == True or self.spacecraft.crash == True:
            self.next_level()

        if self.spacecraft.fuel > 0 and self.spacecraft.los == False:
            if self.spacecraft.thrust_y != 0:
                self.thrust.add_thrust((self.spacecraft.lander.sprite.rect.x),
                                       (self.spacecraft.lander.sprite.rect.y),
                                       42,
                                       56,
                                       'South')
                self.thrust.add_thrust((self.spacecraft.lander.sprite.rect.x),
                                       (self.spacecraft.lander.sprite.rect.y),
                                       18,
                                       56,
                                       'South')
            if self.spacecraft.thrust_x > 0:
                self.thrust.add_thrust((self.spacecraft.lander.sprite.rect.x),
                                       (self.spacecraft.lander.sprite.rect.y),
                                       5,
                                       26,
                                       'West')
            if self.spacecraft.thrust_x < 0:
                self.thrust.add_thrust((self.spacecraft.lander.sprite.rect.x),
                                       (self.spacecraft.lander.sprite.rect.y),
                                       52,
                                       26,
                                       'East')

        self.thrust.update((self.spacecraft.lander.sprite.rect.x),
                            (self.spacecraft.lander.sprite.rect.y))

        if len(self.thrust.particles) > 0:
            self.thrust_group.empty()
            for flame in self.thrust.particles:
                self.thrust_group.add(flame[0])


    def high_score_entry_view(self):
        self.background = (255, 255, 255)
        self.drawable_objects.clear()
        self.drawable_objects.append(self.initials_title)
        self.drawable_objects.append(self.divider)
        self.drawable_objects.append(self.initials_letter0)
        self.drawable_objects.append(self.initials_letter1)
        self.drawable_objects.append(self.initials_letter2)
        self.drawable_objects.append(self.initials_continue)

        self.initials_letter0.redraw_label(text=self.carousel_initials_0.get_selected_item(), color=(200, 200, 200))
        self.initials_letter1.redraw_label(text=self.carousel_initials_0.get_selected_item(), color=(200, 200, 200))
        self.initials_letter2.redraw_label(text=self.carousel_initials_0.get_selected_item(), color=(200, 200, 200))

    def high_score_entry_update(self):
        if self.initials_position < 0:
            self.initials_position = 0
        elif self.initials_position > 2:
            self.initials_position = 2

        if self.initials_position == 0:
            self.initials_letter0.redraw_label(text=self.carousel_initials_0.get_selected_item(), color=(242, 101, 34))
            self.initials_letter1.redraw_label(color=(200, 200, 200))
            self.initials_letter2.redraw_label(color=(200, 200, 200))
        elif self.initials_position == 1:
            self.initials_letter0.redraw_label(color=(200, 200, 200))
            self.initials_letter1.redraw_label(text=self.carousel_initials_1.get_selected_item(), color=(242, 101, 34))
            self.initials_letter2.redraw_label(color=(200, 200, 200))
        elif self.initials_position == 2:
            self.initials_letter0.redraw_label(color=(200, 200, 200))
            self.initials_letter1.redraw_label(color=(200, 200, 200))
            self.initials_letter2.redraw_label(text=self.carousel_initials_2.get_selected_item(), color=(242, 101, 34))

    def view_highscores_view(self):
        self.background = (255, 255, 255)

        up_to_date_scores = high_score_manager.get_high_scores('MarsLanderMars')
        self.top_high_score_label.redraw_label(
            text=str(up_to_date_scores[0]["name"] + "  " + str(up_to_date_scores[0]["score"])))
        self.mid_high_score_label.redraw_label(
            text=str(up_to_date_scores[1]["name"] + "  " + str(up_to_date_scores[1]["score"])))
        self.low_high_score_label.redraw_label(
            text=str(up_to_date_scores[2]["name"] + "  " + str(up_to_date_scores[2]["score"])))

        self.drawable_objects.clear()
        self.drawable_objects.append(self.highscores_title)
        self.drawable_objects.append(self.divider)
        self.drawable_objects.append(self.top_high_score_label)
        self.drawable_objects.append(self.mid_high_score_label)
        self.drawable_objects.append(self.low_high_score_label)
        self.drawable_objects.append(self.initials_continue)

    def view_highscores_update(self):
        pass

    def setup_level(self):
        self.los_group.empty()
        self.score_value_label.redraw_label(text=str(self.score))
        if self.game_mode == 'mars':
            self.spacecraft.set_level(mars_level_data[self.level][0][0],
                                      mars_level_data[self.level][0][1])
            self.planet_surface.new_level(self.level)

    def landing_collision(self):
        if self.spacecraft.crash == True:
            return
        if self.spacecraft.lander.sprite.rect.x <= 29:
            self.spacecraft.deadstick = True
            self.spacecraft.los = True
            self.los_group.add(self.los_label)
            self.los_group.add(self.los_label2)
            self.los_group.add(self.los_rect)
            return
        if self.spacecraft.lander.sprite.rect.x >= 931:
            self.spacecraft.deadstick = True
            self.spacecraft.los = True
            self.los_group.add(self.los_label)
            self.los_group.add(self.los_label2)
            self.los_group.add(self.los_rect)
            return
        if self.spacecraft.lander.sprite.rect.y <= 60:
            self.spacecraft.deadstick = True
            self.spacecraft.los = True
            self.los_group.add(self.los_label)
            self.los_group.add(self.los_label2)
            self.los_group.add(self.los_rect)
            return
        if pygame.sprite.collide_mask(self.spacecraft.lander.sprite, self.planet_surface.terrain.sprite):
            if self.spacecraft.lander.sprite.rect.x > mars_level_data[self.level][1][0] and\
                    self.spacecraft.lander.sprite.rect.x < mars_level_data[self.level][2][0] and\
                    self.spacecraft.lander.sprite.rect.y > mars_level_data[self.level][1][1] and\
                    self.spacecraft.lander.sprite.rect.y < mars_level_data[self.level][2][1]:
                            self.spacecraft.touchdown = True
            else:
                self.spacecraft.crash = True
                self.crash_sound.play()

    def next_level(self):
        if self.spacecraft.collision_cooldown < 30:
            return
        if self.spacecraft.crash == True:
            self.game_state = 'OVER'
            self.handle_event('NONE')
            return
        if self.spacecraft.touchdown == True:
            self.score += int(self.spacecraft.fuel / 7)
            self.fuel.reset()
            self.level += 1
            if self.level == 20:
                self.game_state = 'OVER'
                self.handle_event('NONE')
                return
            self.setup_level()

    def reset_game(self):
        self.score = 0
        self.level = 0
        self.setup_level()
        self.fuel.reset()
        self.spacecraft.set_level(100, 100)
        self.initials_position = 0
        self.carousel_initials_0.set_to_zero_index()
        self.carousel_initials_1.set_to_zero_index()
        self.carousel_initials_2.set_to_zero_index()

    def check_scores(self):
        return high_score_manager.check_if_high_score('MarsLanderMars', self.score)

    def set_score(self):
        high_score_manager.new_high_score('MarsLanderMars', str(self.carousel_initials_0.get_selected_item() +
                                                       self.carousel_initials_1.get_selected_item() +
                                                       self.carousel_initials_2.get_selected_item()),
                                                       self.score)

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