from pygame import Surface
from pygame.sprite import Sprite, OrderedUpdates
from pygame.font import SysFont


class Label(OrderedUpdates):
    """ Use this sprite to write text to the screen.
    """

    DEFAULT_FONT = 'Arial'
    PADDING_SIZE = 5

    def __init__(
        self,
        text_content: str,
        text_color: str,
        text_size: int,
        x_pos: int,
        y_pos: int,
        background_color: str = None,
        font_style: str = DEFAULT_FONT
    ):
        super().__init__()
        self.text_content = text_content
        self.text_color = text_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background_color = background_color
        self.font = SysFont(font_style, text_size)

        self.label = Sprite()
        self.label.image = self.font.render(
            self.text_content,
            True,
            self.text_color
        )
        self.label.rect = self.label.image.get_rect()
        self.label.rect.centerx = self.x_pos
        self.label.rect.centery = self.y_pos

        if background_color:
            self.background = Sprite()
            self.background.image = Surface((
                self.label.rect.width + self.PADDING_SIZE,
                self.label.rect.height + self.PADDING_SIZE
            ))
            self.background.rect = self.background.image.get_rect()
            self.background.rect.centerx = self.x_pos
            self.background.rect.centery = self.y_pos
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