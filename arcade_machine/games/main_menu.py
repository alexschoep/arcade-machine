from pygame import KEYDOWN, K_w, K_s, K_RETURN
from pygame.event import post as pygame_post_event
from pygame.event import Event
from arcade_machine.events import CHANGE_GAME
from arcade_machine.sprites.label import Label
from arcade_machine.games.game import Game
from arcade_machine.components.item_menu import ItemMenu


class MainMenu(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = 'Black'
        menu_title = Label('Arcade Machine', 'White', 40, 400, 100)
        self.drawable_objects.append(menu_title)
        items = [
            "Pong",
            "Game Two"
        ]
        self.menu = ItemMenu(items, 400, 200)
        self.drawable_objects.extend(self.menu.get_item_labels())

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_s:
                self.menu.select_next_item()
            elif event.key == K_w:
                self.menu.select_previous_item()
            elif event.key == K_RETURN:
                item = self.menu.get_selected_item()
                event = Event(CHANGE_GAME, {"game": item})
                pygame_post_event(event)

    def update(self):
        pass