from pygame import Surface
from pygame.sprite import Sprite, OrderedUpdates
from pygame.font import SysFont


class Label(OrderedUpdates):
    """ Use this sprite to write text to the screen.
    """
    PADDING_SIZE = 5

    def __init__(
        self,
        text_content: str,
        text_color: str,
        x_pos: int,
        y_pos: int,
        font,
        background_color: str = None,
        anchor: str = 'Center'
    ):
        super().__init__()
        self.text_content = text_content
        self.text_color = text_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.background_color = background_color
        self.anchor = anchor

        self.label = Sprite()
        self.label.image = self.font.render(
            self.text_content,
            True,
            self.text_color
        )
        self.label.rect = self.label.image.get_rect()
        self.place_label()

        if background_color:
            self.background = Sprite()
            self.background.image = Surface((
                self.label.rect.width + self.PADDING_SIZE,
                self.label.rect.height + self.PADDING_SIZE
            ))
            self.background.rect = self.background.image.get_rect()
            self.place_label()
            self.background.image.fill(self.background_color)

            self.add(self.background)
        
        self.add(self.label)

    def toggle_highlight(self):
        """ Swap text and background color.
        """
        if not self.background_color:
            raise ValueError('label object has no background color')

        swap = self.background_color
        self.background_color = self.text_color
        self.text_color = swap

        self.label.image = self.font.render(
            self.text_content,
            True,
            self.text_color
        )
        self.background.image.fill(self.background_color)

    def redraw_label(
            self,
            text = None,
            color = None,
            font = None
        ):
        if text:
            self.text_content = text
        if color:
            self.text_color = color
        if font:
            self.font = font
        self.label.image = self.font.render(
            self.text_content,
            True,
            self.text_color
        )
        self.label.rect = self.label.image.get_rect()
        self.place_label()

    def place_label(self):
        if self.anchor == "TopLeft":
            self.label.rect = self.label.image.get_rect(topleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidTop":
            self.label.rect = self.label.image.get_rect(midtop=(self.x_pos, self.y_pos))
        elif self.anchor == "TopRight":
            self.label.rect = self.label.image.get_rect(topright=(self.x_pos, self.y_pos))
        elif self.anchor == "MidLeft":
            self.label.rect = self.label.image.get_rect(midleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidRight":
            self.label.rect = self.label.image.get_rect(midright=(self.x_pos, self.y_pos))
        elif self.anchor == "BottomLeft":
            self.label.rect = self.label.image.get_rect(bottomleft=(self.x_pos, self.y_pos))
        elif self.anchor == "MidBottom":
            self.label.rect = self.label.image.get_rect(midbottom=(self.x_pos, self.y_pos))
        elif self.anchor == "BottomRight":
            self.label.rect = self.label.image.get_rect(bottomright=(self.x_pos, self.y_pos))
        else:
            self.label.rect = self.label.image.get_rect(center=(self.x_pos, self.y_pos))