# def max_water(arr):
#     n = len(arr)
#     if n == 0:
#         return 0

#     left_max = [0] * n
#     right_max = [0] * n

#     # Fill left_max
#     left_max[0] = arr[0]
#     for i in range(1, n):
#         left_max[i] = max(arr[i], left_max[i - 1])

#     # Fill right_max
#     right_max[n - 1] = arr[n - 1]
#     for i in range(n - 2, -1, -1):
#         right_max[i] = max(arr[i], right_max[i + 1])

#     # Calculate water
#     res = 0
#     for i in range(n):
#         res += min(left_max[i], right_max[i]) - arr[i]

#     return res


# # Driver code
# arr = [2, 1, 5, 3, 1, 0, 4]
# print(max_water(arr))  # Output: 9



#  Q --ispower

def isPower(x, y):
        # code here
    if x**2==y:
        return True
    return False
x=2
y=8
print(isPower(x,y))
