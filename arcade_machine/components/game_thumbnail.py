from typing import Tuple
from arcade_machine.font_manager import font_manager
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.image_sprite import ImageSprite
from arcade_machine.images.thumbnail_images import *

class GameThumbnail():
    def __init__(
        self,
        title: str,
        thumbnail: Image,
        text_color: Tuple[int, int, int],
        font,
        bg_color: Tuple[int, int, int],
        one_player_mode: bool,
        two_player_mode: bool
    ):
        self.title = title
        self.thumbnail = thumbnail
        self.text_color = text_color
        self.font = font
        self.bg_color = bg_color
        self.one_player_mode = one_player_mode
        self.two_player_mode = two_player_mode

    def get_title(self):
        return self.title

    def get_bg_color(self):
        return self.bg_color

    def get_drawable(self):
        title_sprite = Label(
            self.title,
            self.text_color,
            512,
            610,
            font_manager.get_font(self.font, 48)
        )

        if self.one_player_mode and self.two_player_mode:
            num_players_text = "1 or 2 Players"
        elif self.one_player_mode:
            num_players_text = "Single Player"
        else:
            num_players_text = "Double Player"

        num_players_sprite = Label(
            num_players_text,
            (255, 255, 255),
            512,
            700,
            font_manager.get_font("early_gameboy", 24)
        )

        thumbnail = ImageSprite(
            self.thumbnail,
            512,
            360,
            anchor='Center'
        )

        return [
            title_sprite,
            num_players_sprite,
            thumbnail
        ]


# Game Thumbnails for existing games

pong_thumbnail_item = GameThumbnail(
    "Pong",
    PONG_THUMBNAIL,
    (200, 200, 200),
    "early_gameboy",
    (50, 50, 50),
    True,
    True
)

asteroid_universe_thumbnail_item = GameThumbnail(
    "Asteroid Universe",
    ASTEROID_UNIVERSE_THUMBNAIL,
    (84, 139, 161),
    "racing_hard",
    (16, 48, 61),
    True,
    True
)

mars_lander_thumbnail_item = GameThumbnail(
    "Mars Lander",
    MARS_LANDER_THUMBNAIL,
    (242, 101, 34),
    "lemon_milk",
    (60, 18, 0),
    True,
    False
)

snake_thumbnail_item = GameThumbnail(
    "Snake",
    SNAKE_THUMBNAIL,
    (62, 59, 156),
    "early_gameboy",
    (121, 120, 156),
    True,
    False
)