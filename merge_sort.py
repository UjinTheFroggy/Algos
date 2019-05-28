def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(data):
    if len(data) < 2:
        return data
    middle = round(len(data) / 2)
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])
    return merge(left, right)

data = [3, 4, 7, 2, 9, 6, 1, 8, 5, 0]
print(mergesort(data))
