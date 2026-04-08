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
# def first_occurence(arr,target):
#     start=0
#     stop=len(arr)-1
#     ans=-1
#     while start<=stop:
#         mid=(start+stop)//2
#         if arr[mid]==target:
#             ans=mid
#             stop=mid-1
#         if arr[mid]<target:
#             start=mid+1
#         else:
#             stop=mid-1
#     return  ans

# arr = [1,3,2,2,3]
# target = 2
# print(first_occurence(arr,target))



# Q 4 --> Last occurence
# def last_occurence(arr,target):
#     start=0
#     stop=len(arr)-1
#     ans=-1
#     while start<=stop:
#         mid=(start+stop)//2
#         if arr[mid]==target:
#             ans=mid
#             start=mid+1
#         elif arr[mid]<target:
#             start=mid+1
#         else:
#             stop=mid-1
#     return ans
# arr = [1,2,2,2,3]
# target = 2
# print(last_occurence(arr,target))





# Q 5 --> Search Insert Position (LeetCode 35
# def insert_position(arr,target):
#     start=0
#     stop=len(arr)-1
#     while start<=stop:
#         mid=(start+stop)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             start=mid+1
#         else:
#             stop=mid-1
#     return start
# arr = [1,3,5,6]
# target = 5
# print(insert_position(arr,target))



# Q 6 --> first and last occurence (leetcode 34)
# def first_last(arr,target):
#     first=-1
#     last=-1
#     for i in range(len(arr)):
#         if arr[i]==target:
#             if first==-1:
#                 first=i
#             last=i
            
#     return [first,last]
# arr = [5,7,7,8,8,10]
# target = 8
# print(first_last(arr,target))


# Q 7 -->  Valid Perfect Square (leetcode 367)
def valid_square(num):
    start=0
    stop=num
    while start<=stop:
        mid=(start+stop)//2
        if mid*mid==num:
            return True
        elif mid*mid<num:
            start=mid+1
        else:
            stop=mid-1
    return False
num=12
print(valid_square(num))

