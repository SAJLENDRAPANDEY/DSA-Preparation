# # # # Binary search
# # # def binarySearch( arr, k):
# # #         # code here
        
# # #         left=0
# # #         right=len(arr)-1
# # #         while left<=right:
# # #             mid=(left+right)//2
# # #             if mid==k:
# # #                 return True
                
# # #             elif mid<k:
# # #                 left=mid+1
# # #             else:
# # #                 right=mid-1
# # #         return False
# # # arr=[2,3,4,6]
# # # k=6
# # # print(binarySearch(arr,k))




# # # 647. Palindromic Substrings
# # def countSubstrings( s):

        
# #     count=0
        
# #     for i in range(len(s)):
# #         for j in range(i,len(s)):
# #             substring=s[i:j+1]
# #             left=0
# #             right=len(substring)-1
# #             ispalindrome=True
# #             while left<right:
# #                 if substring[left]!=substring[right]:
# #                     ispalindrome=False
# #                     break
# #                 left+=1
# #                 right-=1

# #             if ispalindrome:
# #                 count+=1
# #     return count
# # print(countSubstrings("abc"))



# # valid anagrams
# def valid_a(s,t):
#     if len(s)!=len(t):
#         return False
#     freq={}
#     for ch in s:
#         freq[ch]=freq.get(ch,0)+1
#         for ch in t:
#             if ch not  in freq:
#                 return False
#         freq[ch]-=ch
#     return True
# s="Hello"
# t="olleH"
# print(valid_a(s,t))



def runningSum(nums):
    i=0
    res=[]
    pre_sum=[0]*len(nums)
    pre_sum[0]=nums[0]
    for j in range(1,len(nums)):
        pre_sum[j]=nums[j-1]+nums[j]
    return pre_sum
nums=[1,2,3]

print(runningSum(nums))
