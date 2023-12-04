file1 = open('input.txt', 'r')
lines = file1.readlines()

result = 0

for line in lines:
    line = line.replace('\n', '')
    game_end_idx = line.index(':')
    set_sep_idx = line.index('|')
    game_id = int([x for x in line[:game_end_idx].split(' ') if x != ''][1])
    raw_sets = line[game_end_idx + 1:].split('|')

    win_set = [int(x) for x in raw_sets[0].split(' ') if x != '']
    player_set = [int(x) for x in raw_sets[1].split(' ') if x != '']

    matches_num = len([w for w in win_set if w in player_set])

    if matches_num > 0:
        result += 2 ** (matches_num - 1)

print(result)
