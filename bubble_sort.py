# question 1 --> Sort the array in ascending order
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[i],arr[j+1]=arr[j+1],arr[i]
#     return arr
# arr=[64, 25, 12, 22, 11]
# print(bubble_sort(arr))

# Question 2 --> sort in descending order 
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]<arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[64, 25, 12, 22, 11]
# print(bubble_sort(arr))

# Question 3 --> Count the number of swaps required to sort
# def count_swaps(arr):
#     n=len(arr)
#     count=0
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 count+=1
#     return (arr ,count)
# arr=[3,2,1]
# print(count_swaps(arr))

# Question 4 --> Find the kth smallest element using Bubble Sort
# def bs(arr,k):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr[k-1]
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(bs(arr,k))


# Question 5 ---> Sort negative and positive numbers
# def bs(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>0  and arr[j+1]<0:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr = [3, -2, 5, -1, 0]
# print(bs(arr))


# Question 6 ---> Sort array with duplicates
# def sort_duplicates(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[2, 3, 2, 1, 3]
# print(sort_duplicates(arr))


# kal lc ke question solve krna h

# Sort array with 1 negative number
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in  range(n-1-i):
#             if arr[j]>0 and arr[j+1]<0:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[5, -3, 2]
# print(sort_arr(arr))

# question 8 Sort array with zeros
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[0, 3, 1]
# print(sort_arr(arr))

# Question 9 -->  

from django.http import HttpRequest
