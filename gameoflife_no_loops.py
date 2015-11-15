from itertools import product
Alive, Dead = True, False
CHECK_RANGE = range(-1, 2)
STATE_TO_STR = {
    Alive: '■',
    Dead: '□',
}

class Game(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_world = World(width, height)
        self.next_world = World(width, height)

    def get(self, x, y):
        return self.current_world.get(x, y)

    def set(self, x, y, value):
        return self.current_world.set(x, y, value)

    def check(self, x, y):
        return self.current_world.check(x, y)

    def change_states(self):
        keys = product(range(0, self.width), range(0, self.height))

        def change_state(el):
            x, y = el
            value = self.current_world.check(x, y)
            self.next_world.set(x, y, value)

        list(map(change_state, keys))
        self.current_world = self.next_world
        self.next_world = World(self.width, self.height)
    
    def __str__(self):
        return str(self.current_world)
        

class World(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.table = list(map(lambda el: [Dead] * height, [None] * width))

    def get(self, x, y):
        xx = x % self.width
        yy = y % self.height
        return self.table[xx][yy]

    def set(self, x, y, value):
        self.table[x][y] = value

    def check(self, x, y):
        keys = product(CHECK_RANGE, repeat=2)
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

    def __str__(self):
        return "\n".join(
            map(
                lambda col: ''.join(
                    map(lambda el: STATE_TO_STR[el], col)
                ),
                self.table, 
            )
        )

