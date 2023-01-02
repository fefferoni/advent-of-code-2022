from pprint import pprint
from queue import Queue
from pathlib import Path

testinput = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def get_input():
    path = Path(__file__).with_name('12.txt')
    with path.open('r') as f:
        return f.read()

input = get_input()

class node:
    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.coor = f'{self.x},{self.y}'
        
    def __str__(self):
        return f'{self.value}'
    def __repr__(self):
        return self.__str__()

class graph:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def elevation(self, coor) -> int:
        x,y = coor.split(',')
        return grid[int(x)][int(y)]

    def neighbors(self, current) -> list:
        neighbors = list()
        if current.x > 0:
            x = current.x - 1
            y = current.y
            val = self.grid[x][y]
            neighbors.append(node(x, y, val))
        if current.x < self.rows - 1:
            x = current.x + 1
            y = current.y
            val = self.grid[x][y]
            neighbors.append(node(x, y, val))
        if current.y > 0:
            x = current.x
            y = current.y - 1
            val = self.grid[x][y]
            neighbors.append(node(x, y, val))
        if current.y < self.cols - 1:
            x = current.x
            y = current.y + 1
            val = self.grid[x][y]
            neighbors.append(node(x, y, val))
        return neighbors

start = node(0, 0, 97)
goal = node(0, 0, 122)

# Find start and goal
for x,r in enumerate(input.splitlines()):
    for y,c in enumerate(r):
        if c == 'S':
            start = node(x, y, 97)
        elif c == 'E':
            goal = node(x, y, 122)

grid = [[ord(x) for x in r] for r in input.replace('E', 'z').splitlines()]
thegraph = graph(grid)

frontier = Queue()
frontier.put(start)
came_from = dict() # path A->B is stored as came_from[B] == A
came_from[start] = None

while not frontier.empty():
   current = frontier.get()
   for next in thegraph.neighbors(current):
      if next.value > current.value + 1:
        continue
      if next.coor not in came_from:
         frontier.put(next)
         came_from[next.coor] = current.coor

# PART ONE
current = goal.coor
path = []
while current != start.coor: 
   path.append(current)
   current = came_from[current]
path.reverse()
print(f'steps part one: {len(path)}')
path.clear()

# PART TWO
current = goal.coor
while thegraph.elevation(current) != 97: 
   path.append(current)
   current = came_from[current]
path.reverse()

# pprint(path)
print(f'steps part two: {len(path)}')
