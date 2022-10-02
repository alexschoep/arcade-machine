from pygame.font import Font as PygameFont


class FontManager:
    font_paths = {
        "early_gameboy": "arcade_machine/resources/fonts/Main Menu/Early GameBoy.ttf",
        "lemon_milk": "arcade_machine/resources/fonts/Mars Lander/LemonMilk.otf",
        "racing_hard": "arcade_machine/resources/fonts/Asteroid Universe/RACING HARD.ttf"
    }

    def __init__(self):
        self.fonts = {}

    def get_font(self, name, size):

        font_family = self.fonts.get(name)

        if not font_family:
            self.fonts[name] = {}
            font = PygameFont(self.font_paths[name], size)
            self.fonts[name][size] = font
            return font

        elif not font_family.get(size):
            font = PygameFont(self.font_paths[name], size)
            font_family[size] = font
            return font
            
        else:
            return font_family[size]

font_manager = FontManager()
