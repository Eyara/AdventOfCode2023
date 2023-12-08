file = open('input.txt', 'r')

lines = file.readlines()

instructions = lines[0].replace('\n', '')
nodes = {}

for line in lines[2:]:
    line = line.replace('\n', '')
    vals = line[line.index('(') + 1:line.index(')')].split(', ')
    nodes[line[:line.index('=') - 1]] = vals

result = 0
was_found = False

current_node_key = 'AAA'

while not was_found:
    for instruction in instructions:
        node_idx = 0 if instruction == 'L' else 1
        current_node_key = nodes[current_node_key][node_idx]
        result += 1

        if current_node_key == 'ZZZ':
            was_found = True
            break

print(result)
