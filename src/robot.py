class Robot:
    def __init__(self, path):
        self.path = path
        self.index = 0

    def move(self):
        if self.index < len(self.path) - 1:
            self.index += 1

    def get_position(self):
        return self.path[self.index]