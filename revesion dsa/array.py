# # # Leetcode 1
# # def two_sum(nums,target):
# #     res=[]
# #     for i in range(len(nums)):
# #         for j in range(i+1,len(nums)):
# #             if nums[i]+nums[j]==target:
# #                 return i, j
# #         i+=1
# #         j+=1
# # arr=[2,3,5,6]
# # target=5
# # print(two_sum(arr,target))


# # Q 2 --> Largest in Array
# # def largest(arr):
# #         # code here
# #         max_e=arr[0]
# #         for i in range(1,len(arr)):
# #             if arr[i]>max_e:
# #                 max_e=arr[i]
# #                 i+=1
# #         return max_e
# # arr=[2,3,4,1,88,9]
# # print(largest(arr))


# def getSecondLargest(arr):
#         largest=num=-1
#         for num in arr:
#             if num>largest:
#                 second=largest
#                 largest=num
#             elif num>second and num!=largest:
#                  second=num
#         return second
# arr=[2,3,4,1,5]
# print(getSecondLargest(arr))




# leetcode (283) moves zero
# def move_zero(arr):
#     left=0
    
#     for right in range(len(arr)):
#         if arr[right]!=0:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
        
#     return arr
# arr=[1,2,32,0,3,0,8]
# print(move_zero(arr))


# leetcode (268)
def missing_number(nums):
    n=len(nums)+1
    expected_sum=(n*(n+1))//2
    total_sum=sum(nums)
    return expected_sum-total_sum
nums=[1,2,3,4,6]
print(missing_number(nums))