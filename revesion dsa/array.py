# # Leetcode 1
# def two_sum(nums,target):
#     res=[]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return i, j
#         i+=1
#         j+=1
# arr=[2,3,5,6]
# target=5
# print(two_sum(arr,target))


# Q 2 --> Largest in Array
def largest(arr):
        # code here
        max_e=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max_e:
                max_e=arr[i]
                i+=1
        return max_e
arr=[2,3,4,1,88,9]
print(largest(arr))