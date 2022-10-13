from pygame import Surface, Rect, SRCALPHA
from pygame.sprite import Sprite, Group
from pygame.draw import polygon as pygame_polygon

class Polygon(Group):

    def __init__(
            self,
            **kwargs):
        super().__init__()
        self.color = kwargs.get('color', (255, 255, 255))
        self.coord_list = kwargs.get('coord_list', [(512, 318), (462, 418), (561, 418)])
        self.x_pos = kwargs.get('x_pos', 100)
        self.y_pos = kwargs.get('y_pos', 100)
        self.line_weight = kwargs.get('line_weight', 0)
        self.alpha = kwargs.get('alpha', 255)
        self.anchor = kwargs.get('anchor', "Center")

        min_x = min(self.coord_list, key=lambda tup: tup[0])[0]
        max_x = max(self.coord_list, key=lambda tup: tup[0])[0]
        self.width = (max_x - min_x)
        min_y = min(self.coord_list, key=lambda tup: tup[1])[1]
        max_y = max(self.coord_list, key=lambda tup: tup[1])[1]
        self.height = (max_y - min_y)

        self.rect = Rect(0, 0, self.width, self.height)

        self.sprite = Sprite()
        self.change_surface_dimension(self.width, self.height)
        self.draw_polygon()
        self.place_polygon()
        self.add(self.sprite)

    def draw_polygon(self):
        pygame_polygon(
            self.sprite.image,
            self.color,
            self.coord_list
        )

    def place_polygon(self):
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
            self.sprite.rect = self.sprite.image.get_rect(center=(self.x_pos, self.y_pos))

    def change_surface_dimension(self, width, height):
        self.surface = Surface((width, height), SRCALPHA, 32)
        self.surface.set_alpha(self.alpha)
        self.surface = self.surface.convert_alpha()
        self.sprite.image = self.surface

    def change_polygon_color(self, new_color):
        self.color = new_color
        self.draw_polygon()

    def change_polygon_position(self, new_x, new_y, new_anchor):
        self.x_pos = new_x
        self.y_pos = new_y
        self.anchor = new_anchor
        self.place_polygon()