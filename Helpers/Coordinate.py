__author__ = 'mateo'


class Coordinate:

    top = 0
    left = 0
    width = 0
    height = 0
    free_left = 0

    def __init__(self, left, top, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def locate(self, left, top):
        return self.left + left, self.top + top

    def get_center(self, width, height):
        return self.left + (self.width - width)/2, self.top + (self.height - height)/2

    def get_vertical_center(self, height):
        return (self.height - height)/2

    def locate_vertical_center(self, left, height):
        return self.left + left, self.top + ((self.height - height)/2)

    def size(self):
        return self.width, self.height

    def size_full(self):
        return self.left, self.top, self.width, self.height

    def get_left(self, offset=0):
        return self.left + offset

    def get_free_left(self, width):
        tmp = self.free_left + self.left
        self.free_left += width
        return tmp

    def get_top(self, offset=0):
        return self.top + offset

    def get_slice(self, width):
        return self.get_free_left(width), self.get_top(), width, self.height

    def get_center_surface(self, width, height):
        return self.left + (self.width - width)/2, self.top + (self.height - height)/2, width, height

    def reset_slice(self):
        self.free_left = 0



