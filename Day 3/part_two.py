def indices(lst, element):
    res = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset + 1)
        except ValueError:
            return res
        res.append(offset)


def get_num(i, j):
    base_str = arr[i][j]

    if j > 0 and arr[i][j - 1].isdigit():
        base_str = arr[i][j - 1] + base_str
        if j - 1 > 0 and arr[i][j - 2].isdigit():
            base_str = arr[i][j - 2] + base_str

    if j < n - 1 and arr[i][j + 1].isdigit():
        base_str += arr[i][j + 1]
        if j < n - 2 and arr[i][j + 2].isdigit():
            base_str += arr[i][j + 2]

    return int(base_str)


file = open('input.txt', 'r')
lines = file.readlines()

result = 0

arr = []
gear_arr = []

for i, line in enumerate(lines):
    line = line.replace('\n', '')
    if '*' in line:
        for j in indices(line, '*'):
            gear_arr.append((i, j))
    arr.append([x for x in line])

n = len(lines)
m = len(lines[0])

for i, j in gear_arr:
    nums = []
    if j < m - 1 and arr[i][j + 1].isdigit():
        nums.append(get_num(i, j + 1))
    if i < n - 1 and arr[i + 1][j].isdigit():
        nums.append(get_num(i + 1, j))
    if i < n - 1 and j < m and arr[i + 1][j + 1].isdigit():
        nums.append(get_num(i + 1, j + 1))
    if i > 0 and arr[i - 1][j].isdigit():
        nums.append(get_num(i - 1, j))
    if i > 0 and j < m - 1 and arr[i - 1][j + 1].isdigit():
        nums.append(get_num(i - 1, j + 1))
    if i < n - 1 and j > 0 and arr[i + 1][j - 1].isdigit():
        nums.append(get_num(i + 1, j - 1))
    if j > 0 and arr[i][j - 1].isdigit():
        nums.append(get_num(i, j - 1))
    if i > 0 and j > 0 and arr[i - 1][j - 1].isdigit():
        nums.append(get_num(i - 1, j - 1))

    nums = list(set(nums))

    if len(nums) == 2:
        result += nums[0] * nums[1]

print(result)
