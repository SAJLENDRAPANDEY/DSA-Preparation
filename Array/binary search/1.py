# Simple Search (Basic)
def binary_search(arr, target):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        mid = (start + stop) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            stop = mid - 1   # left side
        else:
            start = mid + 1  # right side

    return -1


arr = [2, 4, 6, 8, 10]
target = 8
print(binary_search(arr, target))