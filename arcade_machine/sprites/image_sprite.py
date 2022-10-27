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
        self.sprite.image_original = load(image.get_file_path()).convert_alpha()
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
        self.sprite.image_original = load(new_image.get_file_path()).convert_alpha()
        self.sprite.image = load(new_image.get_file_path()).convert_alpha()

    def move_image(self, **kwargs):
        step_x = kwargs.get('step_x')
        step_y = kwargs.get('step_y')
        set_x = kwargs.get('set_x')
        set_y = kwargs.get('set_y')
        anchor = kwargs.get('new_anchor')

        if step_x != None:
            self.x_pos = self.sprite.rect.x + step_x
        if step_y != None:
            self.y_pos = self.sprite.rect.y + step_y
        if set_x != None:
            self.x_pos = set_x
        if set_y != None:
            self.y_pos = set_y

        if anchor != None:
            self.anchor = anchor
        self.place_image()

    def scale_image(self, **kwargs):
        new_size = kwargs.get('new_dim', (100, 100))
        self.sprite.image = scale(self.sprite.image_original, new_size)
        self.sprite.rect = self.sprite.image.get_rect()
        self.place_image()
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)

    def rotate_image(self, **kwargs):
        new_angle = kwargs.get('new_angle', 0)
        self.sprite.image = rotate(self.sprite.image_original, new_angle)
        self.sprite.rect = self.sprite.image.get_rect()
        self.place_image()
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)

