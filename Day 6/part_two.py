file1 = open('input.txt', 'r')
lines = [x.strip().replace('\n', '') for x in file1.readlines()]

time = int(''.join([x for x in lines[0][lines[0].index(':') + 1:].split(' ') if x != '']))
distance = int(''.join([x for x in lines[1][lines[1].index(':') + 1:].split(' ') if x != '']))

result = 0
for i in range(time // 2, time):
    if i * (time - i) > distance:
        result += 1

print(result * 2 - 1)
