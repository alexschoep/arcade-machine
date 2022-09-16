from pygame import Surface, Rect, SRCALPHA
from pygame.sprite import Sprite, Group
from pygame.draw import line as pygame_line

class Line(Group):

    def __init__(
            self,
            **kwargs):
        super().__init__()
        self.color = kwargs.get('color', (255, 255, 255))
        self.start_x_pos = kwargs.get('start_x_pos', 0)
        self.start_y_pos = kwargs.get('start_y_pos', 0)
        self.end_x_pos = kwargs.get('end_x_pos', 50)
        self.end_y_pos = kwargs.get('end_y_pos', 50)
        self.anchor = kwargs.get('anchor', "Start")

        self.width = abs(self.start_x_pos - self.end_x_pos)
        self.height = abs(self.start_y_pos - self.end_y_pos)

        self.sprite = Sprite()
        self.change_surface_dimension(self.width, self.height)
        self.draw_line()
        self.place_line()
        self.add(self.sprite)

    def draw_line(self):
        # Draw rectangle on sprite image -> surface fixed in upper left
        pygame_line(
            self.sprite.image,
            self.color,
            (self.start_x_pos, self.start_y_pos),
            (self.end_x_pos, self.end_y_pos)
        )

    def place_line(self, anchor):
        # Set the surface render to be in the user defined location
        self.sprite.rect = self.sprite.image.get_rect(center=(self.start_x_pos, self.start_y_pos))

    def change_surface_dimension(self, width, height):
        self.surface = Surface((width, height), SRCALPHA, 32)
        self.surface.set_alpha(self.alpha)
        self.surface = self.surface.convert_alpha()
        self.sprite.image = self.surface

    def change_line_dimension(self, new_start_x_pos, new_start_y_pos, new_end_x_pos, new_end_y_pos):
        self.start_x_pos = new_start_x_pos
        self.start_y_pos = new_start_y_pos
        self.end_x_pos = new_end_x_pos
        self.end_y_pos = new_end_y_pos
        self.width = abs(new_start_x_pos - new_end_x_pos)
        self.height = abs(new_start_y_pos - new_end_y_pos)
        self.change_surface_dimension(self.width, self.height)
        self.draw_line()
        self.place_line(self.anchor)

