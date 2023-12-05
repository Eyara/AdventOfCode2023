def get_ranges_from_map(input_map):
    return [(range(x[1], x[1] + x[2]), x[0]) for x in input_map]


def iter_throw_ranges(counter, max_line):
    tmp_lines = []
    while counter < max_line and len(lines[counter].replace('\n', '')) > 0:
        tmp_lines.append([int(x) for x in lines[counter].replace('\n', '').split() if x != ''])
        counter += 1

    return tmp_lines, counter


file1 = open('input.txt', 'r')
lines = file1.readlines()

SEED_TO_SOIL_NAME_TITLE = 'seed-to-soil map:'
SOIL_TO_FERTILIZER_TITLE = 'soil-to-fertilizer map:'
FERTILIZER_TO_WATER_TITLE = 'fertilizer-to-water map:'
WATER_TO_LIGHT_TITLE = 'water-to-light map:'
LIGHT_TO_TEMPERATURE_TITLE = 'light-to-temperature map:'
TEMPERATURE_TO_HUMIDITY_TITLE = 'temperature-to-humidity map:'
HUMIDITY_TO_LOCATION_TITLE = 'humidity-to-location map:'

level_dict = {
    SEED_TO_SOIL_NAME_TITLE: 0,
    SOIL_TO_FERTILIZER_TITLE: 1,
    FERTILIZER_TO_WATER_TITLE: 2,
    WATER_TO_LIGHT_TITLE: 3,
    LIGHT_TO_TEMPERATURE_TITLE: 4,
    TEMPERATURE_TO_HUMIDITY_TITLE: 5,
    HUMIDITY_TO_LOCATION_TITLE: 7
}

seeds = []

map_levels = []
result_seeds = []

for i in range(0, len(lines)):
    line = lines[i].replace('\n', '')
    if 'seeds' in line:
        seeds = [int(x) for x in line[line.index(':') + 1:].split(' ') if x != '']
    elif line in level_dict.keys():
        tmp_lines, counter = iter_throw_ranges(i + 1, len(lines))
        map_levels.append(get_ranges_from_map(tmp_lines))
        i = counter

for seed in seeds:
    current_seed = seed
    for level in map_levels:
        for sub_level in level:
            if current_seed in sub_level[0]:
                current_seed = current_seed + (sub_level[1] - sub_level[0][0])
                break

    result_seeds.append(current_seed)

print(min(result_seeds))
