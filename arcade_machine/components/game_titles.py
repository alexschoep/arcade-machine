
from arcade_machine.components.game_title import GameTitle
from arcade_machine.images.thumbnail_images import pong_thumbnail, no_thumbnail
from arcade_machine.fonts.thumbnail_fonts import early_gameboy_font, lemon_milk_font


pong_carousel_item = GameTitle(
    "Pong",
    pong_thumbnail,
    (200, 200, 200),
    early_gameboy_font,
    (20, 70, 255),
    True,
    True
)

other_carousel_item = GameTitle(
    "Other Game",
    no_thumbnail,
    (200, 200, 200),
    lemon_milk_font,
    (40, 200, 10),
    True,
    False
)