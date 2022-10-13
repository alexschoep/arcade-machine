
class Parallax():

    def __init__(self, sprite):
        self.sprite = sprite
        self.image = self.sprite.sprite.image
        self.image2 = self.sprite.sprite.image.copy()
        self.width, self.height = self.sprite.sprite.image.get_size()

    def scroll(self, scroll_x, scroll_y):
        self.sprite.rect = self.sprite.sprite.image.get_rect()
