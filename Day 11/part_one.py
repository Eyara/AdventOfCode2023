from itertools import accumulate

file = open('input.txt', 'r')

lines = [y for x in file.readlines() for y in x.replace('\n', '').split(' ')]

cols = [[line[i] for line in lines] for i in range(len(lines[0]))]

ys = list(accumulate(1 if "#" in y else 2 for y in lines))
xs = list(accumulate(1 if "#" in x else 2 for x in cols))

galaxy_idxs = [(xs[j], ys[i]) for i, x in enumerate(lines) for j, y in enumerate(x) if y == '#']

n = len(galaxy_idxs)

galaxy_pairs = [(galaxy_idxs[i], galaxy_idxs[j]) for i in range(n) for j in range(i + 1, n)]

result = 0

for first, second in galaxy_pairs:
    result += abs(first[0] - second[0]) + abs(first[1] - second[1])

print(result)
