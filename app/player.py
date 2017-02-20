class Player():

    def __init__(self):
        self.name = "Computer"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_marker(self, mark):
        if mark == ("X" or "O"):
            self.mark = mark
        else:
            raise ValueError

    def get_marker(self):
        return self.mark
