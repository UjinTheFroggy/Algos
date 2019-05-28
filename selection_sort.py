data = [3, 4, 7, 2, 9, 6, 1, 8, 5]

for i in range(len(data) - 1):
    m = i
    j = i + 1
    for j in range(i+1, len(data)):
        if data[j] < data[m]:
            m = j
        j = j + 1
    data[i], data[m] = data[m], data[i]

print(data)
