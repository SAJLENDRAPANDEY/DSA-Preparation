# # Q
# def selection_sort(arr):
#     n=len(arr)
    
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<min_index:
#                 min_index=j
#             arr[i],arr[min_index]=arr[min_index],arr[i]

            
#         return arr
# arr=[5, 3, 1, 4, 2]
# print(selection_sort(arr))


#  Question 1 Sort the array in ascending order
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[4, 2, 5, 1]
# print(sort_arr(arr))

# Question 2 --> Sort the array in descending order
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]>arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[4, 2, 5, 1]
# print(sort_arr(arr))


# Question 3 --> Find the smallest element using Selection Sort
# def find_smallest(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         return arr[min_index]
# arr=[6, 8, 9, 8]
# print(find_smallest(arr))

# Question 4 --> Sort array with negative numbers
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n):
#         min_inx=i
#         for j in range(i+1,n):
#             if arr[j]<0 and  arr[min_inx]>=0:
#                 min_inx=j
#         arr[i],arr[min_inx]=arr[min_inx],arr[i]
#     return arr
# arr=[3, -1, 2, -5]
# print(sort_arr(arr))


# Question 6 --> Find the kth smallest element
# def kth_smallest(arr, k):
#     n = len(arr)
#     for i in range(k):  # Sirf k tak kaam karna hai
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap karo
#     return arr[k-1]  # k-th smallest element (0-based index)

# # Example
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(kth_smallest(arr, k))


# Question 7 --> Reverse sorted array
# def reverse_arr(arr):
#     n=len(arr)
#     for i in range(n-1,-1,-1):
#         print(arr[i],end=" ")
# print(reverse_arr([2,4,6,8]))


# Question 8 --> Sort array with duplicates
# def sort_duplicates(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[2, 2, 1]
# print(sort_duplicates(arr))


# Question 9 ---> Sort array with one negative number
# def sort_arr(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
            

#             if arr[j]< arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[5, -3, 2]
# print(sort_arr(arr))

# Question 10 --> Sort array with zeros
# def sort_arr(arr):

#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# arr=[0, 3, 1]
# print(sort_arr(arr))

# question 11 --> Smallest element at the start
# def smallest_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_inx=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_inx]:
#                 min_inx=j
#         arr[i],arr[min_inx]=arr[min_inx],arr[i]
#     return arr
# arr=[7, 3, 5]
# print(smallest_sort(arr))

# Question 11 --> 