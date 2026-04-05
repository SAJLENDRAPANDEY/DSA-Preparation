# # # prefix sum banao
# # def prefix_sum(arr):
# #     prefix=[0]*len(arr)
# #     prefix[0]=arr[0]
# #     for i in range(1,len(arr)):
# #         prefix[i]=prefix[i-1]+arr[i]
# #     return prefix
# # arr=[1,2,3,4,5,6]
# # print(prefix_sum(arr))



# # Q 2 --> Find sum of entire array using prefix
# # def prefix_sum(arr):
# #     prefix=[0]*len(arr)
# #     prefix[0]=arr[0]
# #     for i in range(1,len(arr)):
# #         prefix[i]=prefix[i-1]+arr[i]
# #     return prefix[-1]
# # arr=[1,2,3]
# # print(prefix_sum(arr))


# # Q 3 --> Count total even numbers using prefix idea
# # def count_even(arr):
# #     prefix=[0]*len(arr)
# #     count=0
# #     prefix[0]= 1 if arr[0]%2==0 else 0
# #     for i in range(1,len(arr)):
# #         if arr[i]%2==0:
# #             prefix[i]=prefix[i-1]+1
# #         else:
# #             prefix[i]=prefix[i-1]
# #     return prefix[-1]
# # arr=[2,3,4,5,6,7,8]
# # p=(count_even(arr))
# # print(p)



# # Q  4 -->Find number of subarrays with sum = K (basic version)
# # def subarray(arr,k):
# #         count=0
# #         for i in range(len(arr)):
# #             s=0
# #             for j in range(i,len(arr)):
# #                 s+=arr[j]
# #                 if s==k:
# #                     count+=1
# #         return count
# # arr=[2,3,2,3]
# # k=5
# # print(subarray(arr,k))

# # Q 5 --> 
# def cntSubarrays(arr, k):
#         # code here
# #         i=0
# #         count=0
        
# #         for i in range(len(arr)):
# #             sum=0
# #             for j in range(i,len(arr)):
                 
# #                 sum+=arr[j]
# #                 if sum==k:
# #                     count+=1
            
# #         return count
# # arr=[10,2,-2,-20,10]
# # k=10
# # print(cntSubarrays(arr,k))


# # optimized version
#     count=0
#     hasmap={0:1}
#     prefix_sum=0
#     for num in arr:
#         prefix_sum+=num
#         if (prefix_sum-k) in hasmap:
#             count+=hasmap[prefix_sum - k]
        
#         hasmap[prefix_sum]=hasmap.get(prefix_sum,0)+1
#     return count

# arr=[10,2,-2,-20,10]
# k=10
# print(cntSubarrays(arr,k))


# subarray sum
# def subarraysum(arr,target):
#     # i=1
#     # left ptr
#     start=0
#     curr=0
#     # right ptr
#     for i in range(len(arr)):
#         curr+=arr[i]

#         while curr>target:
#             curr-=arr[start]
#             start+=1
#         if curr==target:
#             return[start+1,i+1]
#     return -1
    
# arr=[1, 2, 3, 7, 5]
# target = 12
# print(subarraysum(arr,target))



# Leaders in an Array
# def leader(arr):
#     max_l=arr[-1]
#     res=[]
#     res.append(max_l)
#     n=len(arr)
#     for i in range(n-2,-1,-1):
#         if arr[i]>max_l:
#             max_l=arr[i]
#             res.append(arr[i])
#     res.reverse()
#     return res
# arr= [16, 17, 4, 3, 5, 2]
# print(leader(arr))


# Missing Number
def missing_number(arr):
    n=len(arr)+1
    actual_S=n*(n+1)//2
    total_Sum=sum(arr)
    return actual_S-total_Sum
arr=[1,2,3,5]
print(missing_number(arr))
