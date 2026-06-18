# # # q 1 --> Check valid palindrome

# # def valid_pali(s):
# #     left=0
# #     right=len(s)-1
# #     while left<=right:
# #         if not s[left].isalnum():
# #             left+=1
# #             continue
# #         if not s[right].isalnum():
# #             right-=1
# #             continue
# #         if s[left].lower()!=s[right].lower():
# #             return False
        
# #         left+=1
# #         right-=1
# #     return True
# # s="A man, a plan, a canal: Panama "
# # print(valid_pali(s))


# # two sum (lc == 167)
# def two_sum(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         s=arr[left]+arr[right]
#         if s==target:
#             return [arr[left],arr[right]]
#         elif s<target:
#             left+=1
#         else:
#             right-=1
# arr=[2,4,5,6]
# target=10
# print(two_sum(arr,target))


# reverse_string(lc-344)
# def reve_str(s):
#     left=0
#     right=len(s)-1
#     while left<=right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1
#     return s
# s=["h","e","l","l","o"]
# print(reve_str(s))



# or
# def rev_str(s):
#     res=[]
#     for i in range(len(s)-1,-1,-1):
#         res.append(s[i])
#     return "".join(res)
# s="hello"
# print(rev_str(s))



# Q 3 --> Maximum Average Subarray I (lc(643))
def max_arr(arr,k):
    n=len(arr)
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(n-k):
        window_sum=(window_sum-arr[i]+arr[i+k])
        max_sum=max(max_sum,window_sum)
    return (float(max_sum)/k)
arr=[1,12,-5,-6,50,3]
k = 4

print(max_arr(arr,k))