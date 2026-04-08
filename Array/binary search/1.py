# # Simple Search (Basic)
# def binary_search(arr, target):
#     start = 0
#     stop = len(arr) - 1

#     while start <= stop:
#         mid = (start + stop) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             stop = mid - 1   # left side
#         else:
#             start = mid + 1  # right side

#     return -1


# arr = [2, 4, 6, 8, 10]
# target = 8
# print(binary_search(arr, target))


# Q 2-> Element present hai ya nahi
# def binary_search_check(arr,target):
#     start=0
#     stop=len(arr)-1
#     while start<=stop:
#         mid=(start+stop)//2
#         if arr[mid]==target:
#             return True
#         if arr[mid]<target:
#             start=mid+1
#         else:
#             stop=mid-1
#     return False
# arr = [2, 4, 6, 8, 10]
# target = 80
# print(binary_search_check(arr,target))




# Q 3->First Occurrence
def first_occurence(arr,target):
    start=0
    stop=len(arr)-1
    ans=-1
    while start<=stop:
        mid=(start+stop)//2
        if arr[mid]==target:
            ans=mid
            stop=mid-1
        if arr[mid]<target:
            start=mid+1
        else:
            stop=mid-1
    return  ans

arr = [1,3,2,2,3]
target = 2
print(first_occurence(arr,target))