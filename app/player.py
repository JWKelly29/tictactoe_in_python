class Player():

    def __init__(self):
        self.name = "Computer"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarker(self, mark):
        if mark == ("X" or "O"):
            self.mark = mark
        else:
            raise ValueError

    def getMarker(self):
        return self.mark
