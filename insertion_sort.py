data = [3, 4, 7, 2, 9, 6, 1, 8, 5]

for i in range(1, len(data)):
    item_to_insert = data[i]
    j = i - 1
    while j >= 0 and data[j] > item_to_insert:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = item_to_insert

print(data)