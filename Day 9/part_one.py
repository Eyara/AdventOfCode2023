def calc_diff(arr):
    res = []
    for i in range(len(arr) - 1):
        res.append(arr[i + 1] - arr[i])

    return res


file = open('input.txt', 'r')

lines = [x.replace('\n', '').split(' ') for x in file.readlines()]

histories = []
last_vals = []

result = 0

for line in lines:
    histories.append([int(x) for x in line])

for history in histories:
    current_level = history
    last_vals_arr = []
    while True:
        next_level = calc_diff(current_level)
        last_vals_arr.append(next_level[len(next_level) - 1])

        if len(set(next_level)) == 1 and next_level[0] == 0:
            break

        current_level = next_level

    last_vals.append(last_vals_arr)

for i in range(len(histories)):
    n = len(histories[i])
    result += histories[i][n - 1] + sum(last_vals[i])

print(result)
