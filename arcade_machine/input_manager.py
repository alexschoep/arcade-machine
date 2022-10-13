
# Input manager to interpret inputs from keyboard, or joystick(s) and cast them to standard keys for all games to use.
"""
Arcade console to have (1) joystick with 4-directional control and (4) buttons per player.
Each connected joystick will have an instance_id, for this console it is 0, or 1 for (2) players.
The interpretations of the buttons from the keyboard and the joystick(s) are listed:

Button  |  Keyboard  |  Joystick        |  Output
        |  P1, P2    |  P1 (0), P2 (1)  |  Press & Release
-----------------------------------------------------
        |            | AXIS MOTION      |
UP      | K_w, K_i   | 0:1, 1:1         | PX_N_DOWN & PX_NS_UP
DOWN    | K_s, K_k   | 0:1, 1:1         | PX_S_DOWN & PX_NS_UP
LEFT    | K_a, K_j   | 0:0, 1:0         | PX_W_DOWN & PX_EW_UP
RIGHT   | K_d, K_l   | 0:0, 1:0         | PX_E_DOWN & PX_EW_UP
        |            | STANDARD BUTTON  |
A       | K_1, K_7   | 0:0, 1:6         | PX_A_DOWN & PX_A_UP
B       | K_2, K_8   | 0:1, 1:7         | PX_B_DOWN & PX_B_UP
X       | K_3, K_9   | 0:2, 1:8         | PX_X_DOWN & PX_X_UP
Y       | K_4, K_0   | 0:3, 1:9         | PX_Y_DOWN & PX_Y_UP
------------------------------------------------------
PAUSE   | K_p        | 1:5              | PAUSE_DOWN & PAUSE_UP
MENU    | K_m        | 0:4              | MENU_DOWN & MENU_UP
"""
import pygame.joystick
from pygame import KEYDOWN, KEYUP, K_m, K_p, \
    K_1, K_2, K_3, K_4, K_w, K_a, K_s, K_d, \
    K_7, K_8, K_9, K_0, K_i, K_j, K_k, K_l, \
    JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION


class InputManager():
    def __init__(self):
        joysticks = pygame.joystick.get_count()
        if joysticks:
            self.input_mode = 'JOY_CONTROL'
        else:
            self.input_mode = 'KEY_CONTROL'

    def return_event_proxy(self, event):
        if event.type == KEYDOWN: # For down-press keys from the connected keyboard
            # PLAYER 1 INPUTS
            if event.key == K_w:
                return 'P1_N_DOWN'
            if event.key == K_s:
                return 'P1_S_DOWN'
            if event.key == K_a:
                return 'P1_W_DOWN'
            if event.key == K_d:
                return 'P1_E_DOWN'
            if event.key == K_1:
                return 'P1_A_DOWN'
            if event.key == K_2:
                return 'P1_B_DOWN'
            if event.key == K_3:
                return 'P1_X_DOWN'
            if event.key == K_4:
                return 'P1_Y_DOWN'

            # PLAYER 2 INPUTS
            if event.key == K_i:
                return 'P2_N_DOWN'
            if event.key == K_k:
                return 'P2_S_DOWN'
            if event.key == K_j:
                return 'P2_W_DOWN'
            if event.key == K_l:
                return 'P2_E_DOWN'
            if event.key == K_7:
                return 'P2_A_DOWN'
            if event.key == K_8:
                return 'P2_B_DOWN'
            if event.key == K_9:
                return 'P2_X_DOWN'
            if event.key == K_0:
                return 'P2_Y_DOWN'

            # ARCADE CONTROLS
            if event.key == K_m:
                return 'MENU_DOWN'
            if event.key == K_p:
                return 'PAUSE_DOWN'

        if event.type == KEYUP: # For released-press keys from the connected keyboard
            # PLAYER 1 INPUTS
            if event.key == K_w:
                return 'P1_NS_UP'
            if event.key == K_s:
                return 'P1_NS_UP'
            if event.key == K_a:
                return 'P1_EW_UP'
            if event.key == K_d:
                return 'P1_EW_UP'
            if event.key == K_1:
                return 'P1_A_UP'
            if event.key == K_2:
                return 'P1_B_UP'
            if event.key == K_3:
                return 'P1_X_UP'
            if event.key == K_4:
                return 'P1_Y_UP'

            # PLAYER 2 INPUTS
            if event.key == K_i:
                return 'P2_NS_UP'
            if event.key == K_k:
                return 'P2_NS_UP'
            if event.key == K_j:
                return 'P2_EW_UP'
            if event.key == K_l:
                return 'P2_EW_UP'
            if event.key == K_7:
                return 'P2_A_UP'
            if event.key == K_8:
                return 'P2_B_UP'
            if event.key == K_9:
                return 'P2_X_UP'
            if event.key == K_0:
                return 'P2_Y_UP'

            # ARCADE CONTROLS
            if event.key == K_m:
                return 'MENU_UP'
            if event.key == K_p:
                return 'PAUSE_UP'

        if event.type == JOYBUTTONDOWN:
            if event.joy == 0: # PLAYER 1 INPUTS
                if event.button == 0:
                    return 'P1_A_DOWN'
                if event.button == 1:
                    return 'P1_B_DOWN'
                if event.button == 2:
                    return 'P1_X_DOWN'
                if event.button == 3:
                    return 'P1_Y_DOWN'

                if event.button == 4:
                    return 'MENU_DOWN'

            if event.joy == 1:  # PLAYER 2 INPUTS
                if event.button == 6:
                    return 'P2_A_DOWN'
                if event.button == 7:
                    return 'P2_B_DOWN'
                if event.button == 8:
                    return 'P2_X_DOWN'
                if event.button == 9:
                    return 'P2_Y_DOWN'

                if event.button == 5:
                    return 'PAUSE_DOWN'

        if event.type == JOYBUTTONUP:
            if event.joy == 0:  # PLAYER 1 INPUTS
                if event.button == 0:
                    return 'P1_A_UP'
                if event.button == 1:
                    return 'P1_B_UP'
                if event.button == 2:
                    return 'P1_X_UP'
                if event.button == 3:
                    return 'P1_Y_UP'

                if event.button == 4:
                    return 'MENU_UP'

            if event.joy == 1:  # PLAYER 2 INPUTS
                if event.button == 6:
                    return 'P2_A_UP'
                if event.button == 7:
                    return 'P2_B_UP'
                if event.button == 8:
                    return 'P2_X_UP'
                if event.button == 9:
                    return 'P2_Y_UP'

                if event.button == 5:
                    return 'PAUSE_UP'

        if event.type == JOYAXISMOTION:
            if event.joy == 0:  # PLAYER 1 INPUTS
                if event.axis == 1:
                    if event.value < -0.25: # NORTH
                        return 'P1_N_DOWN'
                    if event.value > 0.25: # SOUTH
                        return 'P1_S_DOWN'
                    if event.value >= -0.25 and event.value <= 0.25:
                        return 'P1_NS_UP'
                if event.axis == 0:
                    if event.value < -0.25: # WEST
                        return 'P1_W_DOWN'
                    if event.value > 0.25: # EAST
                        return 'P1_E_DOWN'
                    if event.value >= -0.25 and event.value <= 0.25:
                        return 'P1_EW_UP'

            if event.joy == 1:  # PLAYER 2 INPUTS
                if event.axis == 1:
                    if event.value < -0.25:  # NORTH
                        return 'P2_N_DOWN'
                    if event.value > 0.25:  # SOUTH
                        return 'P2_S_DOWN'
                    if event.value >= -0.25 and event.value <= 0.25:
                        return 'P2_NS_UP'
                if event.axis == 0:
                    if event.value < -0.25:  # WEST
                        return 'P2_W_DOWN'
                    if event.value > 0.25:  # EAST
                        return 'P2_E_DOWN'
                    if event.value >= -0.25 and event.value <= 0.25:
                        return 'P2_EW_UP'