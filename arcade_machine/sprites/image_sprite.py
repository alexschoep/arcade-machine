from pygame.sprite import Sprite, OrderedUpdates
from pygame.image import load


class ImageSprite(OrderedUpdates):
    """ Use this sprite to draw an image to the screen.
    """
    def __init__(self, image, x_pos, y_pos, anchor):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.anchor = anchor

        self.sprite = Sprite()
        self.sprite.image = load(image.get_file_path()).convert()
        self.sprite.rect = self.sprite.image.get_rect()
        self.place_image(self.anchor)

        self.add(self.sprite)

    def place_image(self, anchor):
        # Set the surface render to be in the user defined location
        if self.anchor == "TopLeft":
            self.sprite.rect = self.sprite.image.get_rect(topleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidTop":
            self.sprite.rect = self.sprite.image.get_rect(midtop=(self.x_pos, self.y_pos))
        elif self.anchor == "TopRight":
            self.sprite.rect = self.sprite.image.get_rect(topright=(self.x_pos, self.y_pos))
        elif self.anchor == "MidLeft":
            self.sprite.rect = self.sprite.image.get_rect(midleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidRight":
            self.sprite.rect = self.sprite.image.get_rect(midright=(self.x_pos, self.y_pos))
        elif self.anchor == "BottomLeft":
            self.sprite.rect = self.sprite.image.get_rect(bottomleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidBottom":
            self.sprite.rect = self.sprite.image.get_rect(midbottom=(self.x_pos, self.y_pos))
        elif self.anchor == "BottomRight":
            self.sprite.rect = self.sprite.image.get_rect(bottomright=(self.x_pos, self.y_pos))
        else:
            self.sprite.rect = self.sprite.image.get_rect(center = (self.x_pos, self.y_pos))

    def change_image(self, new_image_path):
        self.sprite.image = load(new_image_path).convert()