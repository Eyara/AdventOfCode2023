from functools import reduce


file1 = open('input.txt', 'r')
lines = [x.strip().replace('\n', '') for x in file1.readlines()]

times = [int(x) for x in lines[0][lines[0].index(':') + 1:].split(' ') if x != '']
distances = [int(x) for x in lines[1][lines[1].index(':') + 1:].split(' ') if x != '']

races = list(zip(times, distances))

results = []

for race in races:
    wins = 0
    for i in range(1, race[0]):
        if i * (race[0] - i) > race[1]:
            wins += 1

    results.append(wins)

print(reduce(lambda x, y: x * y, results))
