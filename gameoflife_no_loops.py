from itertools import product
Alive, Dead = True, False

class Game(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_world = World(width, height)
        self.next_world = World(width, height)


class World(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.table = map(lambda el: [Dead] * height, [None] * width)

    def get(self, x, y):
        f = lambda a, b: min(a - 1, max(0, b))
        xx = f(self.width, x)
        yy = f(self.height, y)
        return self.table[xx][yy]

    def set(self, x, y, value):
        return self.table[x][y]

    def check(self, x, y):
        keys = product(range(-1, 2), repeat=2)
        def check_cell(el):
            i, j = el
            return self.get(x + i, y + j) is Alive
        count = sum(map(check_cell, keys))
        state = self.get(x, y)
        decisions = {
            Alive: lambda: count in [3, 4],
            Dead: lambda: count == 3
        }
        return decisions[state]()
