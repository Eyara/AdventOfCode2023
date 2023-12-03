file = open('input.txt', 'r')
lines = file.readlines()

result = 0

arr = []
symbols_arr = ['@', '#', '!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '/', '?', ':', ';', '"', '<', '>']

for line in lines:
    arr.append([x for x in line])

n = len(lines)
m = len(lines[0])

for i in range(0, n):
    current_num = ''
    current_valid = False

    for j in range(0, m):
        if arr[i][j].isdigit():
            current_num += arr[i][j]
            if j < m - 1 and arr[i][j + 1] in symbols_arr \
                    or i < n - 1 and arr[i + 1][j] in symbols_arr \
                    or i < n - 1 and j < m and arr[i + 1][j + 1] in symbols_arr \
                    or i > 0 and arr[i - 1][j] in symbols_arr \
                    or i > 0 and j < m - 1 and arr[i - 1][j + 1] in symbols_arr \
                    or i < n - 1 and j > 0 and arr[i + 1][j - 1] in symbols_arr \
                    or j > 0 and arr[i][j - 1] in symbols_arr \
                    or i > 0 and j > 0 and arr[i - 1][j - 1] in symbols_arr:
                current_valid = True
        else:
            if current_valid:
                result += int(current_num)
            current_num = ''
            current_valid = False

print(result)
