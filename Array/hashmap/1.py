# # Count frequency of elements
# def count_freq(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     return freq
# arr=[1,2,1,1,1,2,2,3,3,4,3,2]
# print(count_freq(arr))


# 2 Find duplicate element
# def find_duplicate(arr):
#     freq={}
#     res=[]
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     for num in freq:
#         if freq[num]>=2:
#             res.append(freq[num])
#     return res
# arr=[1,1,1,2,2,1,2,3,4,4,3,6]
# print(find_duplicate(arr))



# 3 --> First repeating element
# def first_repeat(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 return i+1
            
#     return -1
    
# arr=[1,2,3,4,2]
# print(first_repeat(arr))


# 4-->Two Sum (leetcode 1)
# def two_sum(arr,target):
#     seen={}
#     for i in range(len(arr)):
#         complement=target-arr[i]

#         if complement in seen:
#             return (seen[complement],i)
    
#         seen[arr[i]]=i
# arr=[2,3,4,2,4]
# target=5
# print(two_sum(arr,target))


# 5 -->Majority Element(leetcode 169)
# def majority_ele(arr):
#     n=len(arr)
#     seen={}
#     for num in arr:
#         seen[num]=seen.get(num,0)+1

#         if seen[num]>n//2:
#             return num
# arr=[2,2,1,1,1,2,2]
# print(majority_ele(arr))


# 6-->
def longestConsecutive( nums):
        
    if not nums:
        return 0
    num_Set=set(nums)
    longest=0

    for num in num_Set:
        if num-1 not in num_Set:
            current_num=num
            count=1

            while current_num+1 in num_Set:
                current_num+=1
                count+=1
        longest=max(longest,count)
    return longest




nums=[100,4,200,1,3,2]
print(longestConsecutive(nums))