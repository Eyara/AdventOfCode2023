file1 = open('input.txt', 'r')
lines = file1.readlines()

result = 0

n = len(lines)

d = {}

for i in range(n):
    d[i] = 1

for i, line in enumerate(lines):
    line = line.replace('\n', '')
    game_end_idx = line.index(':')
    set_sep_idx = line.index('|')
    game_id = int([x for x in line[:game_end_idx].split(' ') if x != ''][1])
    raw_sets = line[game_end_idx + 1:].split('|')

    win_set = [int(x) for x in raw_sets[0].split(' ') if x != '']
    player_set = [int(x) for x in raw_sets[1].split(' ') if x != '']

    matches_num = len([w for w in win_set if w in player_set])

    current_iter = i + 1

    while matches_num > 0 and current_iter < n:
        d[current_iter] += d[i]
        current_iter += 1
        matches_num -= 1

print(sum(d.values()))
