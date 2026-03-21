# def quick_sort(arr):
#     x=len(arr)
#     if x<=1:
#         return arr
#     pivot=arr[0]
#     left=[x for x in arr[1:] if x<pivot]
#     # mid_e =(x for x in arr[1:] if x=pivot)
#     right=[x for x in arr[1:] if x>=pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr=[3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(arr))


# Question 1 --> Sort array with negative numbers
# def Quick_sort(arr):
#     n=len(arr)
#     if n<=1:
#         return arr
#     pivot=arr[0]
#     left=[x for x in arr[1:] if x<pivot]
#     middle=[x for x in arr if x==pivot]
#     right=[x for x in arr[1:] if x>pivot]
#     return Quick_sort(left)+middle+Quick_sort(right)
# arr=[5, -1, 3]
# print(Quick_sort(arr))

# Question 2 -->  Sort array in descending order
def Quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<pivot]
    middle=[x for x in arr if  x==pivot]
    right=[x for x in arr[1:] if x>pivot]
    return Quick_sort(right)+middle+Quick_sort(left)
arr=[2, 5, 1, 3]
print(Quick_sort(arr))