
from arcade_machine.games.game import Game
from pygame import joystick
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.rectangle import Rectangle
from arcade_machine.sprites.ellipse import Ellipse
from arcade_machine.sprites.polygon import Polygon
from arcade_machine.controllers.music_player import set_volume, get_volume
from arcade_machine.controllers.sound_player import set_volume as set_sound_volume
from arcade_machine.events import CHANGE_GAME
from pygame import quit as pygame_quit
from pygame.event import post as pygame_post_event
from pygame.event import Event
from pygame.sprite import Group

from arcade_machine.font_manager import font_manager
from arcade_machine.controllers.music_player import load_music, play_music, stop_music

class KeyboardGraphic():
    def __init__(self):
        self.button_group = Group()
        # LINE 1
        self.rect001 = Rectangle(width=34, height= 34, x_pos=212, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect001)
        self.p1A_btn = Rectangle(width=34, height= 34, x_pos=252, y_pos=380, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1A_btn)
        self.p1B_btn = Rectangle(width=34, height= 34, x_pos=292, y_pos=380, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1B_btn)
        self.p1X_btn = Rectangle(width=34, height= 34, x_pos=332, y_pos=380, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1X_btn)
        self.p1Y_btn = Rectangle(width=34, height= 34, x_pos=372, y_pos=380, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1Y_btn)
        self.rect002 = Rectangle(width=34, height=34, x_pos=412, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect002)
        self.rect003 = Rectangle(width=34, height=34, x_pos=452, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect003)
        self.p2A_btn = Rectangle(width=34, height=34, x_pos=492, y_pos=380, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2A_btn)
        self.p2B_btn = Rectangle(width=34, height=34, x_pos=532, y_pos=380, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2B_btn)
        self.p2X_btn = Rectangle(width=34, height=34, x_pos=572, y_pos=380, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2X_btn)
        self.p2Y_btn = Rectangle(width=34, height=34, x_pos=612, y_pos=380, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2Y_btn)
        self.rect004 = Rectangle(width=34, height=34, x_pos=652, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect004)
        self.rect005 = Rectangle(width=34, height=34, x_pos=692, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect005)
        self.rect006 = Rectangle(width=74, height=34, x_pos=732, y_pos=380, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect006)
        # LINE 2
        self.rect007 = Rectangle(width=50, height=34, x_pos=212, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect007)
        self.rect008 = Rectangle(width=34, height=34, x_pos=268, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect008)
        self.p1N_btn = Rectangle(width=34, height=34, x_pos=308, y_pos=420, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1N_btn)
        self.rect009 = Rectangle(width=34, height=34, x_pos=348, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect009)
        self.rect010 = Rectangle(width=34, height=34, x_pos=388, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect010)
        self.rect011 = Rectangle(width=34, height=34, x_pos=428, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect011)
        self.rect012 = Rectangle(width=34, height=34, x_pos=468, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect012)
        self.rect013 = Rectangle(width=34, height=34, x_pos=508, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect013)
        self.p2N_btn = Rectangle(width=34, height=34, x_pos=548, y_pos=420, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2N_btn)
        self.rect014 = Rectangle(width=34, height=34, x_pos=588, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect014)
        self.pause_btn = Rectangle(width=34, height=34, x_pos=628, y_pos=420, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.pause_btn)
        self.rect016 = Rectangle(width=34, height=34, x_pos=668, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect016)
        self.rect017 = Rectangle(width=34, height=34, x_pos=708, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect017)
        self.rect018 = Rectangle(width=58, height=34, x_pos=748, y_pos=420, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect018)
        # LINE 3
        self.rect019 = Rectangle(width=62, height=34, x_pos=212, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect019)
        self.p1W_btn = Rectangle(width=34, height=34, x_pos=280, y_pos=460, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1W_btn)
        self.p1S_btn = Rectangle(width=34, height=34, x_pos=320, y_pos=460, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1S_btn)
        self.p1E_btn = Rectangle(width=34, height=34, x_pos=360, y_pos=460, color=(80, 10, 15), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p1E_btn)
        self.rect020 = Rectangle(width=34, height=34, x_pos=400, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect020)
        self.rect021 = Rectangle(width=34, height=34, x_pos=440, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect021)
        self.rect022 = Rectangle(width=34, height=34, x_pos=480, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect022)
        self.p2W_btn = Rectangle(width=34, height=34, x_pos=520, y_pos=460, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2W_btn)
        self.p2S_btn = Rectangle(width=34, height=34, x_pos=560, y_pos=460, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2S_btn)
        self.p2E_btn = Rectangle(width=34, height=34, x_pos=600, y_pos=460, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.p2E_btn)
        self.rect023 = Rectangle(width=34, height=34, x_pos=640, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect023)
        self.rect024 = Rectangle(width=34, height=34, x_pos=680, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect024)
        self.rect025 = Rectangle(width=86, height=34, x_pos=720, y_pos=460, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect025)
        # LINE 4
        self.rect026 = Rectangle(width=76, height=34, x_pos=212, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect026)
        self.rect027 = Rectangle(width=34, height=34, x_pos=294, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect027)
        self.rect028 = Rectangle(width=34, height=34, x_pos=334, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect028)
        self.rect029 = Rectangle(width=34, height=34, x_pos=374, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect029)
        self.rect030 = Rectangle(width=34, height=34, x_pos=414, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect030)
        self.rect031 = Rectangle(width=34, height=34, x_pos=454, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect031)
        self.rect032 = Rectangle(width=34, height=34, x_pos=494, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect032)
        self.menu_btn = Rectangle(width=34, height=34, x_pos=534, y_pos=500, color=(4, 46, 77), bevel=5, anchor='TopLeft')
        self.button_group.add(self.menu_btn)
        self.rect033 = Rectangle(width=34, height=34, x_pos=574, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect033)
        self.rect034 = Rectangle(width=34, height=34, x_pos=614, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect034)
        self.rect035 = Rectangle(width=34, height=34, x_pos=654, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect035)
        self.rect036 = Rectangle(width=112, height=34, x_pos=694, y_pos=500, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect036)
        # LINE 5
        self.rect037 = Rectangle(width=36, height=34, x_pos=212, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect037)
        self.rect038 = Rectangle(width=34, height=34, x_pos=254, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect038)
        self.rect039 = Rectangle(width=34, height=34, x_pos=294, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect039)
        self.rect040 = Rectangle(width=34, height=34, x_pos=334, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect040)
        self.rect041 = Rectangle(width=234, height=34, x_pos=374, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect041)
        self.rect042 = Rectangle(width=34, height=34, x_pos=614, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect042)
        self.rect043 = Rectangle(width=34, height=34, x_pos=654, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect043)
        self.rect044 = Rectangle(width=34, height=34, x_pos=694, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect044)
        self.rect045 = Rectangle(width=72, height=34, x_pos=734, y_pos=540, color=(100, 100, 100), bevel=5, anchor='TopLeft')
        self.button_group.add(self.rect045)

    def colorize(self, object, color):
        object.change_rectangle_color(color)

class JoystickGraphic():
    def __init__(self):
        self.button_group = Group()
        self.menu_btn = Ellipse(width=30, height=30, x_pos=470, y_pos=400, color=(80, 10, 15))
        self.button_group.add(self.menu_btn)
        self.pause_btn = Ellipse(width=30, height=30, x_pos=554, y_pos=400, color=(4, 46, 77))
        self.button_group.add(self.pause_btn)
        self.p1N_btn = Polygon(color=(80, 10, 15), coord_list=[(15, 0), (0, 30), (30, 30)], x_pos=240, y_pos=470)
        self.button_group.add(self.p1N_btn)
        self.p1S_btn = Polygon(color=(80, 10, 15), coord_list=[(0, 0), (30, 0), (15, 30)], x_pos=240, y_pos=570)
        self.button_group.add(self.p1S_btn)
        self.p1E_btn = Polygon(color=(80, 10, 15), coord_list=[(0, 0), (30, 15), (0, 30)], x_pos=290, y_pos=520)
        self.button_group.add(self.p1E_btn)
        self.p1W_btn = Polygon(color=(80, 10, 15), coord_list=[(30, 0), (30, 30), (0, 15)], x_pos=190, y_pos=520)
        self.button_group.add(self.p1W_btn)
        self.p1A_btn = Ellipse(width=30, height=30, x_pos=400, y_pos=570, color=(80, 10, 15))
        self.button_group.add(self.p1A_btn)
        self.p1B_btn = Ellipse(width=30, height=30, x_pos=450, y_pos=520, color=(80, 10, 15))
        self.button_group.add(self.p1B_btn)
        self.p1X_btn = Ellipse(width=30, height=30, x_pos=350, y_pos=520, color=(80, 10, 15))
        self.button_group.add(self.p1X_btn)
        self.p1Y_btn = Ellipse(width=30, height=30, x_pos=400, y_pos=470, color=(80, 10, 15))
        self.button_group.add(self.p1Y_btn)
        self.p2N_btn = Polygon(color=(4, 46, 77), coord_list=[(15, 0), (0, 30), (30, 30)], x_pos=624, y_pos=470)
        self.button_group.add(self.p2N_btn)
        self.p2S_btn = Polygon(color=(4, 46, 77), coord_list=[(0, 0), (30, 0), (15, 30)], x_pos=624, y_pos=570)
        self.button_group.add(self.p2S_btn)
        self.p2E_btn = Polygon(color=(4, 46, 77), coord_list=[(0, 0), (30, 15), (0, 30)], x_pos=674, y_pos=520)
        self.button_group.add(self.p2E_btn)
        self.p2W_btn = Polygon(color=(4, 46, 77), coord_list=[(30, 0), (30, 30), (0, 15)], x_pos=574, y_pos=520)
        self.button_group.add(self.p2W_btn)
        self.p2A_btn = Ellipse(width=30, height=30, x_pos=784, y_pos=570, color=(4, 46, 77))
        self.button_group.add(self.p2A_btn)
        self.p2B_btn = Ellipse(width=30, height=30, x_pos=834, y_pos=520, color=(4, 46, 77))
        self.button_group.add(self.p2B_btn)
        self.p2X_btn = Ellipse(width=30, height=30, x_pos=734, y_pos=520, color=(4, 46, 77))
        self.button_group.add(self.p2X_btn)
        self.p2Y_btn = Ellipse(width=30, height=30, x_pos=784, y_pos=470, color=(4, 46, 77))
        self.button_group.add(self.p2Y_btn)

    def colorize(self, object, color):
        if type(object) is Ellipse:
            object.change_ellipse_color(color)
        elif type(object) is Polygon:
            object.change_polygon_color(color)

class ArcadeSettings(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = (0, 0, 0)
        self.volume = get_volume()
        if joystick.get_count():
            self.input_mode = 'JOYSTICK'
            self.control_display = JoystickGraphic()
        else:
            self.input_mode = 'KEYBOARD'
            self.control_display = KeyboardGraphic()

        self.TITLE_FONT = font_manager.get_font("early_gameboy", 48)
        self.BODY_FONT = font_manager.get_font("early_gameboy", 24)

        self.settings_title = Label('Settings', (255, 255, 255), 512, 60, self.TITLE_FONT)
        self.ver_text = Label('Version: 0.0.1', (100, 100, 100), 100, 180, self.BODY_FONT, anchor='MidLeft')
        self.vol_text = Label('System Volume:', (100, 100, 100), 100, 240, self.BODY_FONT, anchor='MidLeft')
        self.vol_level = Label(str(int(self.volume * 100)), (255, 255, 255), 440, 240, self.BODY_FONT, anchor='MidLeft')

        self.controls_text = Label('System Controls:', (100, 100, 100), 100, 330, self.BODY_FONT, anchor='MidLeft')
        self.controls_mode = Label(self.input_mode, (255, 255, 255), 500, 330, self.BODY_FONT, anchor='MidLeft')

        self.back = Label("Press 'A' to return to the games.", (120, 120, 120), 512, 660, self.BODY_FONT)
        self.leave = Label('Press MENU to quit the console.', (80, 10, 15), 512, 700, self.BODY_FONT)
        self.creators = Label('By Alex and Billy', (40, 40, 40), 512, 740, self.BODY_FONT)



        self.divider = Rectangle(color=(255, 255, 255), x_pos=0, y_pos=120, width=1024, height=4, line_weight=4,
                                bevel=0, alpha=255,anchor="TopLeft")

        self.bar_outline = Rectangle(color=(65, 65, 65), x_pos=512, y_pos=280, width=800, height=30, line_weight=2,
                                      bevel=5, alpha=255, anchor="Center")

        self.fill_bar = Rectangle(color=(10, 80, 65), x_pos=116, y_pos=280, width=int(self.volume * 792), height=22, line_weight=0,
                                     bevel=3, alpha=255, anchor="MidLeft")


        self.control_outline = Rectangle(color=(65, 65, 65),
                                     x_pos=512,
                                     y_pos=360,
                                     width=800,
                                     height=250,
                                     line_weight=2,
                                     bevel=5,
                                     alpha=255,
                                     anchor="MidTop")
        self.drawable_objects.append(self.control_outline)

        self.drawable_objects.append(self.settings_title)  # Add labels to be drawn
        self.drawable_objects.append(self.ver_text)
        self.drawable_objects.append(self.vol_text)
        self.drawable_objects.append(self.vol_level)
        self.drawable_objects.append(self.controls_text)
        self.drawable_objects.append(self.controls_mode)
        self.drawable_objects.append(self.back)
        self.drawable_objects.append(self.leave)
        self.drawable_objects.append(self.creators)
        self.drawable_objects.append(self.fill_bar)
        self.drawable_objects.append(self.bar_outline)
        self.drawable_objects.append(self.divider)

        self.drawable_objects.append(self.control_display.button_group)

        load_music('arcade_machine/resources/audio/Settings/menu_music.mp3')
        play_music()  # loop indefinitely

    def handle_event(self, event):
        if event == 'P1_W_DOWN' or event == 'P2_W_DOWN':
            self.handle_change_volume('DOWN')
        elif event == 'P1_E_DOWN' or event == 'P2_E_DOWN':
            self.handle_change_volume("UP")
        elif event ==  'P1_A_DOWN' or event == 'P2_A_DOWN':
            stop_music()
            event = Event(CHANGE_GAME, {"game": "MainMenu"})
            pygame_post_event(event)
            return
        elif event == 'MENU_DOWN':
            stop_music()
            pygame_quit()
            exit()
        self.highlight_controls(event)
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

    def highlight_controls(self, event):
        print(event)
        if event == 'PAUSE_DOWN':
            self.control_display.colorize(self.control_display.pause_btn, (126,173,208))
        if event == 'PAUSE_UP':
            self.control_display.colorize(self.control_display.pause_btn, (4, 46, 77))

        # Player 1 Controls
        if event == 'P1_N_DOWN':
            self.control_display.colorize(self.control_display.p1N_btn, (221,84,84))
        if event == 'P1_NS_UP':
            self.control_display.colorize(self.control_display.p1N_btn, (80, 10, 15))
            self.control_display.colorize(self.control_display.p1S_btn, (80, 10, 15))
        if event == 'P1_S_DOWN':
            self.control_display.colorize(self.control_display.p1S_btn, (221,84,84))
        if event == 'P1_E_DOWN':
            self.control_display.colorize(self.control_display.p1E_btn, (221,84,84))
        if event == 'P1_EW_UP':
            self.control_display.colorize(self.control_display.p1E_btn, (80, 10, 15))
            self.control_display.colorize(self.control_display.p1W_btn, (80, 10, 15))
        if event == 'P1_W_DOWN':
            self.control_display.colorize(self.control_display.p1W_btn, (221,84,84))
        if event == 'P1_A_DOWN':
            self.control_display.colorize(self.control_display.p1A_btn, (221,84,84))
        if event == 'P1_A_UP':
            self.control_display.colorize(self.control_display.p1A_btn, (80, 10, 15))
        if event == 'P1_B_DOWN':
            self.control_display.colorize(self.control_display.p1B_btn, (221,84,84))
        if event == 'P1_B_UP':
            self.control_display.colorize(self.control_display.p1B_btn, (80, 10, 15))
        if event == 'P1_X_DOWN':
            self.control_display.colorize(self.control_display.p1X_btn, (221,84,84))
        if event == 'P1_X_UP':
            self.control_display.colorize(self.control_display.p1X_btn, (80, 10, 15))
        if event == 'P1_Y_DOWN':
            self.control_display.colorize(self.control_display.p1Y_btn, (221,84,84))
        if event == 'P1_Y_UP':
            self.control_display.colorize(self.control_display.p1Y_btn, (80, 10, 15))

        # Player 2 Controls
        if event == 'P2_N_DOWN':
            self.control_display.colorize(self.control_display.p2N_btn, (126,173,208))
        if event == 'P2_NS_UP':
            self.control_display.colorize(self.control_display.p2N_btn, (4, 46, 77))
            self.control_display.colorize(self.control_display.p2S_btn, (4, 46, 77))
        if event == 'P2_S_DOWN':
            self.control_display.colorize(self.control_display.p2S_btn, (126,173,208))
        if event == 'P2_E_DOWN':
            self.control_display.colorize(self.control_display.p2E_btn, (126,173,208))
        if event == 'P2_EW_UP':
            self.control_display.colorize(self.control_display.p2E_btn, (4, 46, 77))
            self.control_display.colorize(self.control_display.p2W_btn, (4, 46, 77))
        if event == 'P2_W_DOWN':
            self.control_display.colorize(self.control_display.p2W_btn, (126,173,208))
        if event == 'P2_A_DOWN':
            self.control_display.colorize(self.control_display.p2A_btn, (126,173,208))
        if event == 'P2_A_UP':
            self.control_display.colorize(self.control_display.p2A_btn, (4, 46, 77))
        if event == 'P2_B_DOWN':
            self.control_display.colorize(self.control_display.p2B_btn, (126,173,208))
        if event == 'P2_B_UP':
            self.control_display.colorize(self.control_display.p2B_btn, (4, 46, 77))
        if event == 'P2_X_DOWN':
            self.control_display.colorize(self.control_display.p2X_btn, (126,173,208))
        if event == 'P2_X_UP':
            self.control_display.colorize(self.control_display.p2X_btn, (4, 46, 77))
        if event == 'P2_Y_DOWN':
            self.control_display.colorize(self.control_display.p2Y_btn, (126,173,208))
        if event == 'P2_Y_UP':
            self.control_display.colorize(self.control_display.p2Y_btn, (4, 46, 77))