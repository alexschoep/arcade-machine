from pygame.font import Font as PygameFont

class Font:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path