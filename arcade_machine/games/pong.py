from pygame import KEYDOWN, KEYUP, K_RETURN, K_w, K_s, K_i, K_k
from pygame.event import post as pygame_post_event
from pygame.event import Event
from arcade_machine.events import CHANGE_GAME
from pygame import Surface
from pygame.sprite import Sprite, Group
from arcade_machine.games.game import Game
from arcade_machine.sprites.label import Label
from arcade_machine.font_manager import font_manager
from pygame.font import Font as PygameFont

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1024


class Ball(Group):
    INITIAL_SPEED = 5
    RADIUS = 20

    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        super().__init__()
        self.sprite = Sprite()
        self.sprite.image = Surface((self.RADIUS, self.RADIUS))
        self.sprite.image.fill('Red')
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x_pos
        self.sprite.rect.y = y_pos
        self.add(self.sprite)

        self.x_vel = x_vel
        self.y_vel = 0

    def update(self):
        self.sprite.rect.centery += self.y_vel
        self.sprite.rect.centerx += self.x_vel

        if self.sprite.rect.centery + self.RADIUS >= SCREEN_HEIGHT:
            self.sprite.rect.centery = SCREEN_HEIGHT - self.RADIUS
            self.y_vel = - self.y_vel
            return
        
        if self.sprite.rect.centery - self.RADIUS <= 0:
            self.sprite.rect.centery = 0 + self.RADIUS
            self.y_vel = - self.y_vel

    def handle_collision(self):
        self.x_vel = - self.x_vel
        self.increment_speed()

    def increment_speed(self):
        self.x_vel += 1 if self.x_vel > 0 else -1
        self.y_vel += 1 if self.y_vel > 0 else -1



class Paddle(Group):
    MOVEMENT_SPEED = 20
    OFFSET = 10
    WIDTH = 20
    HEIGHT = 100
    RADIUS = HEIGHT / 2

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.sprite = Sprite()
        self.sprite.image = Surface((self.WIDTH, self.HEIGHT))
        self.sprite.image.fill('White')
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.centerx = x_pos
        self.sprite.rect.centery = y_pos
        self.add(self.sprite)

        self.y_vel = 0

    def set_velocity(self, direction):
        if direction == 'UP':
            self.y_vel = -self.MOVEMENT_SPEED
        elif direction == 'DOWN':
            self.y_vel = self.MOVEMENT_SPEED
        else:
            self.y_vel = 0

    def update(self):
        self.sprite.rect.centery += self.y_vel

        if self.sprite.rect.centery + self.RADIUS >= SCREEN_HEIGHT:
            self.sprite.rect.centery = SCREEN_HEIGHT - self.RADIUS

        elif self.sprite.rect.centery - self.RADIUS <= 0:
            self.sprite.rect.centery = 0 + self.RADIUS


class Pong(Game):
    def __init__(
        self
    ):
        super().__init__()

    def initialize(self):
        self.game_state = 'LAUNCH'
        self.background = 'Black'

    def handle_event(self, event):
        if self.game_state == 'VICTORY':
            if event.type == KEYDOWN:
                self.game_state = 'LAUNCH'

        elif self.game_state == 'PLAY':
            self.handle_play_event(event)

    def handle_play_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                event = Event(CHANGE_GAME, {"game": "MainMenu"})
                pygame_post_event(event)
            elif event.key == K_w:
                self.left_paddle.set_velocity('UP')
            elif event.key == K_s:
                self.left_paddle.set_velocity('DOWN')
            elif event.key == K_i:
                self.right_paddle.set_velocity('UP')
            elif event.key == K_k:
                self.right_paddle.set_velocity('DOWN')
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                self.left_paddle.set_velocity(0)
            if event.key == K_i or event.key == K_k:
                self.right_paddle.set_velocity(0)

    def update(self):
        if self.game_state == 'LAUNCH':
            self.ball = Ball(400, 400, -Ball.INITIAL_SPEED, Ball.INITIAL_SPEED)

            self.left_paddle = Paddle(
                Paddle.WIDTH / 2 + Paddle.OFFSET, SCREEN_HEIGHT / 2)
            self.right_paddle = Paddle(
                SCREEN_WIDTH - Paddle.WIDTH / 2 - Paddle.OFFSET, SCREEN_HEIGHT / 2)
            
            self.drawable_objects.clear()
            self.drawable_objects.extend([
                self.ball,
                self.left_paddle,
                self.right_paddle
            ])
            self.game_state = 'PLAY'
            return

        elif self.game_state == 'PLAY':
            self.ball.update()        
            self.left_paddle.update()
            self.right_paddle.update()

            result = self.detect_collision()
            if result != 'no_collision':
                if result == 'left_deflect':
                    self.ball.handle_collision()
                elif result == 'right_deflect':
                    self.ball.handle_collision()
                elif result == 'left_miss':
                    self.game_state = 'VICTORY'
                    self.winner = 'right'
                elif result == 'right_miss':
                    self.game_state = 'VICTORY'
                    self.winner = 'left'
            return

        elif self.game_state == 'VICTORY':
            self.handle_victory()

    def detect_collision(self) -> str:
        if self.ball.sprite.rect.centerx <= (Paddle.WIDTH + Paddle.OFFSET + Ball.RADIUS):
            if self.ball.sprite.rect.centery >= (self.left_paddle.sprite.rect.centery - Paddle.RADIUS) \
                    and self.ball.sprite.rect.centery <= (self.left_paddle.sprite.rect.centery + Paddle.RADIUS):
                return 'left_deflect'
            else:
                return 'left_miss'

        elif self.ball.sprite.rect.centerx >= (SCREEN_WIDTH - Paddle.WIDTH - Paddle.OFFSET - Ball.RADIUS):
            if self.ball.sprite.rect.centery >= (self.right_paddle.sprite.rect.centery - Paddle.RADIUS) \
                    and self.ball.sprite.rect.centery <= (self.right_paddle.sprite.rect.centery + Paddle.RADIUS):
                return 'right_deflect'
            else:
                return 'right_miss'

        else:
            return 'no_collision'

    def handle_victory(self):
        victory_label = Label(
            "Game Over",
            (255,255,255),
            500,
            400,
            font_manager.get_font('early_gameboy', 48)
        )
        self.drawable_objects.append(victory_label)