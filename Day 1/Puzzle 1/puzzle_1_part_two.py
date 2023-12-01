file1 = open('input.txt', 'r')
lines = file1.readlines()

result_arr = []

for line in lines:
    replaced_line = line.replace("twone", "21").replace("sevenine", "79") \
        .replace("oneight", "18").replace("threeight", "38") \
        .replace("nineight", "98").replace("fiveight", "58") \
        .replace("eighthree", "83").replace("eightwo", "82") \
        .replace('one', '1') \
        .replace('two', '2').replace('three', '3').replace('four', '4') \
        .replace('five', '5').replace('six', '6').replace('seven', '7') \
        .replace('eight', '8').replace('nine', '9')

    n = len(replaced_line)
    i = 0
    digit_arr = []

    for i in replaced_line:
        if i.isdigit():
            digit_arr.append(i)

    if len(digit_arr) > 1:
        result_arr.append(int(digit_arr[0] + digit_arr[len(digit_arr) - 1]))
    else:
        result_arr.append(int(digit_arr[0] * 2))

print(sum(result_arr))
