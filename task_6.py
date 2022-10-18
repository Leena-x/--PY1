list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_index = list(range(len(list_numbers)))

now_index = 0
for i in list_index:
    max_n = list_numbers[now_index]
    current_n = list_numbers[i]
    if current_n > max_n:
        now_index = i

list_numbers[now_index], list_numbers[19] = list_numbers[19], list_numbers[now_index]
print(list_numbers)
