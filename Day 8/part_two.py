import math


def get_count_step(current_key, instructions):
    was_found = False
    steps = 0
    current_node_key = current_key
    while not was_found:
        for instruction in instructions:
            node_idx = 0 if instruction == 'L' else 1
            current_node_key = nodes[current_node_key][node_idx]
            steps += 1

            if current_node_key.endswith('Z'):
                was_found = True
                break

    return steps


file = open('input.txt', 'r')

lines = file.readlines()

instructions = lines[0].replace('\n', '')
nodes = {}

for line in lines[2:]:
    line = line.replace('\n', '')
    vals = line[line.index('(') + 1:line.index(')')].split(', ')
    nodes[line[:line.index('=') - 1]] = vals

start_nodes = [x for x in list(nodes.keys()) if x.endswith('A')]

results = [get_count_step(x, instructions) for x in start_nodes]

print(math.lcm(*results))
