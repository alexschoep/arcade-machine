from pygame import KEYDOWN, K_RETURN
from pygame.event import post as pygame_post_event
from pygame.event import Event
from arcade_machine.events import CHANGE_GAME
from pygame import Surface
from pygame.sprite import Sprite, Group
from arcade_machine.games.game import Game
from arcade_machine.sprites.rectangle import Rectangle


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((10, 10))
        self.image.fill('Red')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        self.rect.x += 1
        self.rect.y += 0


class Pong(Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.background = 'Black'
        ball = Ball()
        self.ball_group = Group()
        self.ball_group.add(ball)
        self.drawable_objects.append(self.ball_group)

        r = Rectangle(color=(0, 255, 0),
                      x_pos=400,
                      y_pos=100,
                      width=50,
                      height=80,
                      line_weight=2,
                      bevel=5,
                      alpha=80,
                      anchor="BottomRight")
        self.drawable_objects.append(r)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)

    def update(self):
        self.ball_group.update()