from pygame import QUIT, mouse
from pygame import init as pygame_init
from pygame import quit as pygame_quit
from pygame.display import set_mode as pygame_set_display_mode
from pygame.display import update as pygame_update_display
from pygame.time import Clock
from pygame.event import get as pygame_get_event
from pygame.joystick import Joystick
from arcade_machine.input_manager import InputManager

from arcade_machine.events import CHANGE_GAME
from games.main_menu import MainMenu
from games.arcade_settings import ArcadeSettings
from games.pong import Pong
from games.snake import Snake
from games.mars_lander import MarsLander
from games.asteroid_universe import AsteroidUniverse

from arcade_machine.controllers.music_player import stop_music

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

def main():
    pygame_init()
    clock = Clock()
    screen = pygame_set_display_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#, FULLSCREEN) TODO: Implement FULLSCREEN
    mouse.set_visible(False)

    current_game = None
    current_game_title = "MainMenu"
    game_changed = True

    try: # Setup Joysticks for input
        player1 = Joystick(0)
        player2 = Joystick(1)
    except:
        pass
    input_manager = InputManager()

    while True:
        if game_changed:
            stop_music() # Stop music to prevent sound mix issues when initializing the next game
            current_game = get_game(current_game_title)
            current_game.initialize()
            game_changed = False

        for event in pygame_get_event():
            if event.type == QUIT:
                pygame_quit()
                exit()
            elif event.type == CHANGE_GAME:
                game_changed = True
                current_game_title = event.game
            else:
                current_game.handle_event(input_manager.return_event_proxy(event))
        
        if not game_changed:
            current_game.update()
            current_game.draw_screen(screen)
            
            pygame_update_display()
            clock.tick(30)

def get_game(game_title):
    games = {
        "MainMenu": MainMenu(),
        "Pong": Pong(),
        "Settings": ArcadeSettings(),
        "Snake": Snake(),
        "Mars Lander": MarsLander(),
        "Asteroid Universe": AsteroidUniverse()
    }
    return games[game_title]

if __name__ == "__main__":
    main()
