def binary_search(lst, x):
    lst.sort()
    low = 0
    high = len(lst) - 1
    answer = None
    while low <= high:
        mid = (low + high) // 2
        print(f"{low} – {mid} – {high}")
        if lst[mid] == x:
            answer = mid
            break
        elif lst[mid] > x:
            high = mid - 1
        elif lst[mid] < x:
            low = mid + 1
	
    return answer

if __name__ == '__main__':
	print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 0), sep='\n')