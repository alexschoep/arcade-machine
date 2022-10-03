
class CarouselMenu():
    def __init__(self, items):
        self.items = items
        self.selected_item_index = 0

    def select_next_item(self):
        self.selected_item_index += 1
        if self.selected_item_index > len(self.items) - 1:
            self.selected_item_index = 0
        return self.items[self.selected_item_index]

    def select_previous_item(self):
        self.selected_item_index -= 1
        if self.selected_item_index < 0:
            self.selected_item_index = len(self.items) - 1
        return self.items[self.selected_item_index]

    def get_selected_item(self):
        return self.items[self.selected_item_index]

    def set_to_zero_index(self):
        try:
            self.selected_item_index = 0
        except:
            pass
