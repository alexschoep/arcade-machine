from pygame.sprite import Sprite
from pygame import draw
from pygame import Surface
from pygame import mask

def rect_sprite(dimensions, **kwargs):
    shape = Sprite()
    shape.image = Surface([1024, 12])
    draw.rect(shape.image, (255, 255, 255), dimensions)
    shape.rect = shape.image.get_rect()
    shape.rect.centerx = 512
    shape.rect.centery = 360

    if "mask" in kwargs:
        cutout = mask.from_surface(shape.image)
        return shape, cutout
    return shape


if __name__ == "__main__":
    pass