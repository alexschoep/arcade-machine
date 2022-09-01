from pygame import image, font
from pygame.sprite import Sprite

class GameTitle():
    def __init__(self, title, image_path, text_color, font_path, bg_color, players):
        self.title = title
        self.poster = image_path
        self.text_color = text_color
        self.font_face = font.Font(font_path, 60)
        self.bg_color = bg_color
        self.players = players # 0 - Both, 1 - Single Only, 2 - Two Players Only

