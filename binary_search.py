# # 1 linear search

# # Search an element in array

# # Input: arr = [2, 5, 8, 9], target = 8

# # Output: 2 (index of 8)
# # def linear_search(arr,target):
# #     for i in range(len(arr)):
# #         if arr[i]==target:
# #             return i
# #     return None
# # print(linear_search([2,3,21,5],0))


# # question 2 --> Find index of first occurrence
# # def find_index(arr,target):
# #     for i in  range(len(arr)):
# #         if arr[i]==target:
# #             return i
# #     return None
# # print(find_index([3,2,4,2,1],2))

# # question 3 ---> Find index of second occurrence
# # def find_index(arr,target):
# #     for i in  range(len(arr)-1,-1,-1):
# #         if arr[i]==target:
# #             return i
# #     return None
# # print(find_index([3,2,4,2,1,0],2))

# # question 4 --> Count occurrences of an element 
# # def count_occurence(arr,target):
# #     count=0
# #     for i in  range(len(arr)):
# #         if arr[i]==target:
# #             count+=1
# #             # i+=1
    
# #     return count
# # print(count_occurence([2,2,23,4,2,1,2],2))

# # question 5 --> Find maximum element using linear search
# # def max_element(arr):
# #     if len(arr)==0:
# #         return None
# #     max_val=arr[0]
# #     for i in range(1,len(arr)):
# #         if arr[i]>max_val:
# #             max_val=arr[i]
# #     return max_val
        
# # print(max_element([2,4,2,1,8,9]))

# # question 6 --> Find minimum element using linear search
# # def min_element(arr):
# #     if len(arr)==0:
# #         return None
# #     min_ele=arr[0]
# #     for i in range(len(arr)):
# #         if arr[i]<min_ele:
# #             min_ele=arr[i]
# #     return min_ele
# # print(min_element([2,4,2,1,8,9]))

# # question 7 --> Find Minimum and Maximum using Linear Search
# def min_max_elem(arr):
#     min_ele=arr[0]
#     max_ele=arr[0]
#     if len(arr)==0:
#         return 0
#     for i in range(len(arr)):
#         if arr[i]>max_ele:
#             max_ele=arr[i]
#         if arr[i]<min_ele:
#             min_ele=arr[i]

#     return max_ele
#     #return min_ele

# print(min_max_elem([2,4,2,1,8,9]))


# question 8 ---> Check if Array Contains Negative Number
# def check_neg(arr):
#     for i in range(len(arr)):
#         if arr[i]<0:
#             print("yes found at index", i)
#             return
#     print("not found")
# print(check_neg([3, 7, -2, 8, 5]))

# question 9 --> Find Index of First Even Number
# def even_number(arr):
#     for i in range(len(arr)):
#         if arr[i]%2==0:
#             return (i)
# print(even_number([1, 3, 7, 8, 5]))


# question 10  --> Find element in sorted array
# def bs(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i 
# arr=[1,3,5,7,9,11]
# target=7
# print(bs(arr,target))

# question 11- Find first and last position of element in sorted array
# def first_last(arr):
#     left=0
#     for right in range(len(arr)):
#         if arr[right]==arr[left]:
#             return (left,right)
        


# question 13 ---> . Find Peak Element
# def peak_element(arr):
#     if len(arr)==1:
#         return arr[0]
#     for i in range(1,len(arr)-1):
#         if arr[i-1]<arr[i]>arr[i+1]:
#             return arr[i]
#     if arr[0]>arr[1]:
#         return arr[0]
#     if arr[-1]>arr[-2]:
#         return arr[-1]
#     return None
# print(peak_element([2,3,5,6]))



# question 13 -- binary search question 
# def bs(arr,target):
#     start,end=0,len(arr)-1
#     while (start<=end):
#         mid=(start+end)//2
#         if arr[mid]==target:
#             return mid
#         elif target>mid:
#             start=mid+1
#         elif target<mid:
#             end=mid-1
#     return -1

# arr=[2,3,4,6,9]
# target=6
# print(bs(arr,target))

# question 14 --> Search Insert Position (LC 35)
# def insert_position(arr,target):
#     low=0
#     high=len(arr)-1
#     while low <=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif target>arr[mid]:
#             low=mid+1
#         else:
#             high=mid-1
#     return low
# arr = [1, 3, 5, 6]
# target = 4
# print(insert_position(arr,target))

# question 15--> Valid Perfect Square
# def perfect_sqr(num):
#     low=1
#     high=num//2
#     while (low<=high):
#         mid=(low+high)//2
#         if mid*mid==num:
#             return True
#         elif mid*mid<num:
#             low=mid+1
#         else:
#             high=mid-1
#     return False
# print(perfect_sqr(16))  # True
# print(perfect_sqr(14)) 

# question 16 --> Smallest Number Greater Than Target
# def smallest_greater(arr,target):
#     low=0
#     high=len(arr)-1
#     ans=None
#     while(low<=high):
#         mid=(low+high)//2
#         if arr[mid]>target:
#             ans=arr[mid]
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# print(smallest_greater([2,3,5,7,9,10],7))


# question 17 --> Square Root of a Number
# def sqr_number(x):
#     if x<2:
#         return x
#     low=1
#     high=x//2
#     ans=1
    
#     while (low<=high):
#         mid=(low+high)//2
#         sqr=mid*mid
#         if sqr==x:
#             return mid
#         elif sqr<x:
#             ans=mid
#             low=mid+1
#         else:
#             high=mid-1
#     return ans
# print(sqr_number(9))

# binary search easy question 

# aBST me search element