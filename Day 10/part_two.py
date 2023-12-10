import sys

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def calc_new_idx(old, new):
    return old[0] + new[0], old[1] + new[1]


def get_borders(current_idx, step, direction, indexes=None):
    if indexes is None:
        indexes = []

    indexes.append(current_idx)

    cur_point = lines[current_idx[0]][current_idx[1]]
    if cur_point == '|':
        if direction == 'up':
            return get_borders(calc_new_idx(current_idx, (-1, 0)), step + 1, direction, indexes)
        elif direction == 'down':
            return get_borders(calc_new_idx(current_idx, (1, 0)), step + 1, direction, indexes)
    elif cur_point == '-':
        if direction == 'left':
            return get_borders(calc_new_idx(current_idx, (0, -1)), step + 1, direction, indexes)
        elif direction == 'right':
            return get_borders(calc_new_idx(current_idx, (0, 1)), step + 1, direction, indexes)
    elif cur_point == 'L':
        if direction == 'left':
            return get_borders(calc_new_idx(current_idx, (-1, 0)), step + 1, 'up', indexes)
        elif direction == 'down':
            return get_borders(calc_new_idx(current_idx, (0, 1)), step + 1, 'right', indexes)
    elif cur_point == 'J':
        if direction == 'right':
            return get_borders(calc_new_idx(current_idx, (-1, 0)), step + 1, 'up', indexes)
        elif direction == 'down':
            return get_borders(calc_new_idx(current_idx, (0, -1)), step + 1, 'left', indexes)
    elif cur_point == '7':
        if direction == 'right':
            return get_borders(calc_new_idx(current_idx, (1, 0)), step + 1, 'down', indexes)
        elif direction == 'up':
            return get_borders(calc_new_idx(current_idx, (0, -1)), step + 1, 'left', indexes)
    elif cur_point == 'F':
        if direction == 'up':
            return get_borders(calc_new_idx(current_idx, (0, 1)), step + 1, 'right', indexes)
        elif direction == 'left':
            return get_borders(calc_new_idx(current_idx, (1, 0)), step + 1, 'down', indexes)
    elif cur_point == 'S':
        return indexes


def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{!r} is not in list".format(search))


file = open('input.txt', 'r')

sys.setrecursionlimit(100000)

lines = [y for x in file.readlines() for y in x.replace('\n', '').split(' ')]

n = len(lines)
m = len(lines[0])

start_idx = index_2d(lines, 'S')

start_offset = [('up', -1, 0), ('left', 0, -1), ('down', 1, 0), ('right', 0, 1)]

borders = []
for offset in start_offset:
    new_idx = start_idx[0] + offset[1], start_idx[1] + offset[2]

    if new_idx[0] < 0 or new_idx[1] < 0:
        continue

    if offset[0] == 'up':
        if lines[new_idx[0]][new_idx[1]] in ('|', '7', 'F'):
            borders.append(get_borders(new_idx, 1, offset[0]))
    elif offset[0] == 'left':
        if lines[new_idx[0]][new_idx[1]] in ('-', 'F', 'L'):
            borders.append(get_borders(new_idx, 1, offset[0]))
    elif offset[0] == 'down':
        if lines[new_idx[0]][new_idx[1]] in ('|', 'J', 'L'):
            borders.append(get_borders(new_idx, 1, offset[0]))
    elif offset[0] == 'right':
        if lines[new_idx[0]][new_idx[1]] in ('_', 'J', '7'):
            borders.append(get_borders(new_idx, 1, offset[0]))

polygon = Polygon(borders[0])

result = 0

for i in range(n):
    for j in range(m):
        if (i, j) not in borders[0]:
            point = Point(i, j)
            if polygon.contains(point):
                result += 1

print(result)
