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
# def valid_square(num):
#     start=0
#     stop=num
#     while start<=stop:
#         mid=(start+stop)//2
#         if mid*mid==num:
#             return True
#         elif mid*mid<num:
#             start=mid+1
#         else:
#             stop=mid-1
#     return False
# num=12
# print(valid_square(num))




















# Valid Perfect Square (oractice)
# def valid_square(num):
#     start=1
#     stop=num
#     while start<=stop:
#         mid=(start+stop)//2
#         if mid*mid==num:
#             return True
#         elif num*num<mid:
#             start=mid+1
#         else:
#             stop=mid-1
#     return False
# num=16
# print(valid_square(num))



# Q 2 --> Peak Index in a Mountain Array (Leetcode 852)

# def peak_element(arr):
#     n=len(arr)
#     if n==1:
#         return 0
#     if arr[0]>arr[1]:
#         return 0
#     if arr[n-1]>arr[n-2]:
#         return n-1
#     for i in range(1,n-1):
#         if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#             return i

# arr=[0,1,3,0]
# print(peak_element(arr))



# Q 3 --> Count Frequency
# def count_freq(arr,target):
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==target:
#             count+=1
#     return count
# arr=[1, 1, 2, 2, 2, 2, 3]
# target = 2
# print(count_freq(arr,target))



# Q 4 --> find floor 
# def floor(arr,x):
#     n=len(arr)
#     if x>=arr[n-1]:
#         return n-1
#     elif arr[0]>x:
#         return -1
#     ans=-1
#     for i in range(0,n):
#         if arr[i]>=x:
#             return i-1
#     return ans
# arr= [1, 2, 8, 10, 10, 12, 19]
# x = 11
# print(floor(arr,x))




# Q 5 -->  Single Element in a Sorted Array (Leetcode 540)
# def sorted_arr(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     for num in freq:
#         if freq[num]==1:
#             return  num
# arr = [1,1,2,3,3,4,4,8,8]
# print(sorted_arr(arr))



# Q 6 --> Square Root of a Number(gfg)

def floorSqrt(n): 
        # code here
    start=1
    stop=n
    ans=0
    while start<=stop:
        mid=(start+stop)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            start=mid+1
            ans=mid
        else:
            stop=mid-1
    return ans
n=16
print(floorSqrt(n))
                
                