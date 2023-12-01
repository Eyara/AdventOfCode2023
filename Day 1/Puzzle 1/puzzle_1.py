file1 = open('input.txt', 'r')
lines = file1.readlines()

result_arr = []


for line in lines:
    n = len(line)
    i = 0
    digit_arr = []

    for i in line:
        if i.isdigit():
            digit_arr.append(i)

    if len(digit_arr) > 1:
        result_arr.append(int(digit_arr[0] + digit_arr[len(digit_arr) - 1]))
    else:
        result_arr.append(int(digit_arr[0] * 2))

print(sum(result_arr))
