

class Carousel():
    def __init__(self):
        self.objects = []
        self.current_object = 0
        self.num_objects = 0
        pass

    def add_object(self, new_object):
        self.objects.append(new_object)
        self.num_objects = (len(self.objects) - 1)

    def increment(self):
        self.current_object += 1
        if self.current_object > self.num_objects:
            self.current_object = 0

    def decrement (self):
        self.current_object -= 1
        if self.current_object < 0:
            self.current_object = self.num_objects