from pygame import image, font
from pygame.sprite import Sprite

class Title():
    def __init__(self, title, image_path, text_color, font_path, bg_color, players):
        self.title = title
        self.poster = Sprite()
        self.poster.image = image.load(image_path).convert()
        self.poster.rect = self.poster.image.get_rect()
        self.poster.rect.centerx = 512
        self.poster.rect.centery = 360

        self.text_color = text_color
        self.font_face = font.Font(font_path, 60)
        self.bg_color = bg_color
        self.players = players # 0 - Both, 1 - Single Only, 2 - Two Players Only

if __name__ == "__main__":
    pass
