from pygame import Surface, Rect, SRCALPHA
from pygame.sprite import Sprite, Group
from pygame.draw import rect as pygame_rect

class Rectangle(Group):

    def __init__(
            self,
            **kwargs):
        super().__init__()
        self.color = kwargs.get('color', (255, 255, 255))
        self.x_pos = kwargs.get('x_pos', 100)
        self.y_pos = kwargs.get('y_pos', 100)
        self.width = kwargs.get('width', 100)
        self.height = kwargs.get('height', 100)
        self.line_weight = kwargs.get('line_weight', 0)
        self.bevel = kwargs.get('bevel', 0)
        self.alpha = kwargs.get('alpha', 255)
        self.anchor = kwargs.get('anchor', "Center")

        self.rect = Rect(0, 0, self.width, self.height)

        self.sprite = Sprite()
        self.change_surface_dimension(self.width, self.height)
        self.draw_rectangle()
        self.place_rectangle()
        self.add(self.sprite)

    def draw_rectangle(self):
        # Draw rectangle on sprite image -> surface fixed in upper left
        pygame_rect(
            self.sprite.image,
            self.color,
            self.rect,
            self.line_weight,
            self.bevel
        )

    def place_rectangle(self):
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

    def change_surface_dimension(self, width, height):
        self.surface = Surface((width, height), SRCALPHA, 32)
        self.surface.set_alpha(self.alpha)
        self.surface = self.surface.convert_alpha()
        self.sprite.image = self.surface

    def change_rectangle_dimension(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.change_surface_dimension(self.width, self.height)
        self.draw_rectangle()
        self.place_rectangle()

    def change_rectangle_color(self, new_color):
        self.color = new_color
        self.draw_rectangle()

    def change_rectangle_position(self, new_x, new_y, new_anchor):
        self.x_pos = new_x
        self.y_pos = new_y
        self.anchor = new_anchor
        self.place_rectangle()


