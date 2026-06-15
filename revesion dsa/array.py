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
# def missing_number(nums):
#     n=len(nums)+1
#     expected_sum=(n*(n+1))//2
#     total_sum=sum(nums)
#     return expected_sum-total_sum
# nums=[1,2,3,4,6]
# print(missing_number(nums))



# Leetcode (238)
# def mult_a(arr):
#     n=len(arr)
#     result=[]
#     i=0
#     for i in range(n):
#         total=1
#         for j in  range(n):
            
#             if i!=j:
#                 total*=arr[j]
#         result.append(total)
            
#     return result
# arr=[2,3,1]
# print(mult_a(arr))




# Leetcode (169)
# def majority_ele(arr):
#     n=len(arr)
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1

#         if freq[num]>n//2:
#             return num
# arr=[2,2,1,1,1,2,2]
# print(majority_ele(arr))



# moves zero end
# def moves_zero(arr):
#     left=0
#     for right in range(len(arr)):
#         if arr[right]!=0:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
#     return arr
# arr=[1,3,0,3,0,8]
# print(moves_zero(arr))


# missing number
# def missing_number(arr):
#     n=len(arr)
#     actual_sum=(n*(n+1))//2
#     predicted_sum=sum(arr)
#     return predicted_sum-actual_sum
# arr=[1,3,4]
# print(missing_number(arr))


# majority element (size len(arr)//2  se jyada ho  ) 
# def majority_ele(arr):
#     n=len(arr)
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1

#         if freq[num]>n//2:
#             return num
#     return -1
# arr=[3,2,3,2,2,4,4,4,4,4,5]
# print(majority_ele(arr))



# Leetcode (242)( Valid Anagram)
# def valid_anagram(s,t):
#     if len(s)!=len(t):
#         return False
#     freq={}
#     for ch in s:
#         freq[ch]=freq.get(ch,0)+1
#     for ch in t:
#         if ch not in freq or freq[ch]==0:
#             return False
#         freq[ch]-=1
#     return True
# s="Anagram"
# t="margnaA"
# print(valid_anagram(s,t))


# leetcode (217. Contains Duplicate)

# def check_dupli(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1

   
#     if freq[num]>1:
#         return True
#     return False
# arr=[2,3,3,3]
# print(check_dupli(arr))


# Frequencies in a Limited Array


# def frequencyCount(arr):
#         #  code here
#         freq={}
#         for num in arr:
#             freq[num]=freq.get(num,0)+1
            
#         res=[]
#         N=len(arr)
#         for i in range(1,N+1):
#             res.append(freq.get(i,0))
#         return res
# arr= [2, 3, 2, 3, 5]
# print(frequencyCount(arr))


# Leetcode 217 (Contains Duplicate)
# def check_duplicate(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     for num in freq:
#         if freq[num]>1:
#             return True
#     return False
# arr=[2,3,4]
# print(check_duplicate(arr))



# 
# def check_duplicate_arr(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     for num in freq:
#         if freq[num]>1:
#             return True
#     return False
# arr=[2,3,4,4]
# print(check_duplicate_arr(arr))



# leetcode 34
# def check(arr,target):
#     first=-1
#     last=-1
#     for i in range(len(arr)):
#         if arr[i]==target:
#             if first==-1:
#                 first=i
#             last=i
#     return [first,last]
# arr=[2,2,3,4,4,5,5,5,5,5,6]
# target=5
# print(check(arr,target))



# Subarray Sum Equals K (lc=560)
def subarray(arr,k):
    count=0
    for i in range(len(arr)):
        total=0
        for j in range(i,len(arr)):
            total+=arr[j]
            if total==k:
                count+=1
    return count
arr=[2,3,2,4,2]
k=4
print(subarray(arr,k))