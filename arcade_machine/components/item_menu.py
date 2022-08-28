from arcade_machine.sprites.label import Label

class ItemMenu():
    TEXT_SIZE = 30
    ITEM_SPACING = 40

    def __init__(self, items, x_offset, y_offset):
        self.items = items
        self.item_labels = []
        item_index = 0

        for item in self.items:
            label = Label(
                item,
                'White',
                self.TEXT_SIZE,
                x_offset,
                item_index * self.ITEM_SPACING + y_offset,
                background_color='Black'
            )
            self.item_labels.append(label)
            item_index += 1

        self.selected_item_index = 0
        self.item_labels[self.selected_item_index].toggle_highlight()
        
    def get_item_labels(self):
        return self.item_labels

    def select_next_item(self):
        self.item_labels[self.selected_item_index].toggle_highlight()
        self.selected_item_index += 1
        if self.selected_item_index > len(self.items) - 1:
            self.selected_item_index = 0
        self.item_labels[self.selected_item_index].toggle_highlight()

    def select_previous_item(self):
        self.item_labels[self.selected_item_index].toggle_highlight()
        self.selected_item_index -= 1
        if self.selected_item_index < 0:
            self.selected_item_index = len(self.items) - 1
        self.item_labels[self.selected_item_index].toggle_highlight()

    def get_selected_item(self):
        return self.items[self.selected_item_index]