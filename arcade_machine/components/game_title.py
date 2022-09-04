from typing import Tuple
from pygame.font import Font as PygameFont
from arcade_machine.images.image import Image
from arcade_machine.fonts.font import Font
from arcade_machine.sprites.label import Label
from arcade_machine.sprites.image_sprite import ImageSprite
from arcade_machine.fonts.thumbnail_fonts import early_gameboy_font

class GameTitle():
    def __init__(
        self,
        title: str,
        thumbnail: Image,
        text_color: Tuple[int, int, int],
        font: Font,
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
            650,
            PygameFont(self.font.get_file_path(), 48)
        )

        if self.one_player_mode and self.two_player_mode:
            num_players_text = "One or Two Players"
        elif self.one_player_mode:
            num_players_text = "One Player"
        else:
            num_players_text = "Two Players"

        num_players_sprite = Label(
            num_players_text,
            (255, 255, 255),
            512,
            700,
            PygameFont(early_gameboy_font.get_file_path(), 24)
        )

        thumbnail = ImageSprite(
            self.thumbnail,
            512,
            360,
            "Center"
        )

        return [
            title_sprite,
            num_players_sprite,
            thumbnail
        ]
