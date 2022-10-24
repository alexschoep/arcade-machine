import pygame.mask
from pygame.sprite import Sprite, OrderedUpdates
from pygame.image import load
from pygame.transform import scale, rotate


class ImageSprite(OrderedUpdates):
    """ Use this sprite to draw an image to the screen.
    """
    def __init__(self, image, x_pos, y_pos, anchor):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.anchor = anchor

        self.sprite = Sprite()
        self.sprite.image = load(image.get_file_path()).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.place_image()
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)

        self.add(self.sprite)

    def place_image(self):
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

    def change_image(self, new_image):
        self.sprite.image = load(new_image.get_file_path()).convert_alpha()

    def move_image(self, **kwargs):
        step_x = kwargs.get('step_x', 0)
        step_y = kwargs.get('step_y', 0)
        set_x = kwargs.get('set_x', -1)
        set_y = kwargs.get('set_y', -1)

        if step_x != 0:
            self.sprite.rect.x += step_x
        if step_y != 0:
            self.sprite.rect.y += step_y
        if set_x != -1:
            self.sprite.rect.x = set_x
        if set_y != -1:
            self.sprite.rect.y = set_y

    def scale_image(self, **kwargs):
        new_size = kwargs.get('new_dim', (100, 100))
        self.sprite.image = scale(self.sprite.image, new_size)
        self.sprite.rect = self.sprite.image.get_rect()
        self.place_image()
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)

