class human:
    def __init__ (self, first, last):
        self.first = first
        self.last = last
    def getName(self):
        return self.first + self.last

he = human('matt', 'wan')
print(he.getName())
