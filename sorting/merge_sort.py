# # def merge_sort(arr):
# #     if len(arr)<=1:
# #         return arr
# #     mid=len(arr)//2
# #     left=arr[:mid]
# #     right=arr[mid:]
# #     left=merge_sort(left)
# #     right=merge_sort(right)
# #     return merge(left,right)
# # def merge(left,right):
# #     i=j=0
# #     res=[]
# #     while i<len(left) and j<len(right):
# #         if left[i]<right[j]:
# #             res.append(left[i])
# #             i+=1
# #         else:
# #             res.append(right[j])
# #             j+=1
# #     res.extend(left[i:])
# #     res.extend(right[j:])
# #     return res
# # arr=[5, 3, 8, 1, 2]
# # print("Sorted array",merge_sort(arr))


# # Question 1 --> Sort array with negative numbers
# # def sort_arr(arr):
# #     n=len(arr)
# #     if n<=1:
# #         return arr
# #     mid=len(arr)//2
# #     left=arr[:mid]
# #     right=arr[mid:]
# #     left=sort_arr(left)
# #     right=sort_arr(right)
# #     return merge(left,right)
# # def merge(left,right):
# #     i=j=0
# #     res=[]
# #     while i<len(left) and j<len(right):
# #         if left[i] < right[j]:
# #             res.append(left[i])
# #             i+=1
# #         else:
# #             res.append(right[j])
# #             j+=1
# #     res.extend(left[i:])
# #     res.extend(right[j:])
# #     return res
# # arr=[5, -1, 3]
# # print("merge sort",sort_arr(arr))



# # Question 2 ---> Sort array in descending order
# def merge_sort(arr):
#     n=len(arr)
#     if n<=1:
#         return arr
#     mid =len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     left=merge_sort(left)
#     right=merge_sort(right)
#     return merge(left,right)
# def merge(left,right):
#     i=j=0
#     res=[]
#     while i <len(left) and j<len(right):
#         if left[i]>right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res
# arr=[2, 5, 1, 3]
# print("Sorted arr",merge_sort(arr))




