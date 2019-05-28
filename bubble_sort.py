data = [3, 4, 7, 2, 9, 6, 1, 8, 5]

for i in range(len(data)):
    for j in range(len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
print(data)
