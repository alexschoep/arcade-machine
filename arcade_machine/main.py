from pygame import QUIT
from pygame import init as pygame_init
from pygame import quit as pygame_quit
from pygame.display import set_mode as pygame_set_display_mode
from pygame.display import update as pygame_update_display
from pygame.time import Clock
from pygame.event import get as pygame_get_event
from arcade_machine.events import CHANGE_GAME

from arcade_machine.games.main_menu import MainMenu
from arcade_machine.games.pong import Pong

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def main():
    pygame_init()
    clock = Clock()
    screen = pygame_set_display_mode((
        SCREEN_WIDTH,
        SCREEN_HEIGHT
    ))

    current_game = None
    current_game_title = "MainMenu"
    game_changed = True

    while True:
        if game_changed:
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
                current_game.handle_event(event)
        
        if not game_changed:
            current_game.update()
            current_game.draw_screen(screen)
            
            pygame_update_display()
            clock.tick(30)

def get_game(game_title):
    games = {
        "MainMenu": MainMenu(),
        "Pong": Pong()
    }
    return games[game_title]

if __name__ == "__main__":
    main()