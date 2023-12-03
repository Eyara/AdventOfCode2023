file1 = open('input.txt', 'r')
lines = file1.readlines()

result = 0

for line in lines:
    game_end_idx = line.index(':')
    game_id = int(line[:game_end_idx].split(' ')[1])

    line_arr = line[game_end_idx + 1:].replace('\n', '').split(';')
    cleared_arr = []
    for elem in line_arr:
        cleared_arr.append([x for x in elem.split(' ') if x != ''])

    cleared_arr = [item for sublist in cleared_arr for item in sublist]

    game_valid = True
    i = 0

    while i < len(cleared_arr):
        cube_type = cleared_arr[i + 1].replace(',', '')
        val = int(cleared_arr[i])
        if cube_type == 'red' and val > 12:
            game_valid = False
            break
        elif cube_type == 'green' and val > 13:
            game_valid = False
            break
        elif cube_type == 'blue' and val > 14:
            game_valid = False
            break

        i += 2

    if game_valid:
        result += game_id

print(result)
