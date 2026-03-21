# # # two sum 
# # def two_sum(arr,target):
# #     left=0
# #     right=len(arr)-1
# #     while left<right:
# #         s=arr[left]+arr[right]
# #         if s==target:
# #             return [arr[left],arr[right]]
# #         elif s>target:
# #             right-=1
# #         else:
# #             left+=1
# #     return 0
# # arr=[10,20,30,40,60]
# # print(two_sum(arr,40))



# #  2 --Validpalindrome
# # def valid_che(s):
# #     left=0
# #     right=len(s)-1
# #     while left<right:
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
# # s="A man, a plan, a canal: Panama"
# # print(valid_che(s))


# # complexity o(n)

# # def valid_check(s):
# #     chr=""
# #     for ch in s:
# #         if ch.isalnum():
# #             chr+=ch.lower()
# #     return chr==chr[::-1]
# # s="A man, a plan, a canal: Panama"
# # print(valid_check(s))



















# # # valid palindrome
# # def check_palindrome(s):
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
# #         right+=1
# #     return True
# # s="abac"
# # print(check_palindrome(s))



# #  or logic
# # def valid_palindrome(s):
# #     chr=""
# #     for ch in s:
# #         if ch.isalnum():
# #             chr+=ch.lower()
# #     return chr==chr[::-1]
# # s="abaf"
# # print(valid_palindrome(s))


# # 2 --> moves zeros end
# # def moves_zero(arr):
# #     left=0
# #     for right in range (len(arr)):
# #         if arr[right]!=0:
# #             arr[right],arr[left]=arr[left],arr[right]
# #             left+=1
# #     return arr
# # arr=[2,0,3,0,5,0,8]
# # print(moves_zero(arr))




# # remove duplicates from sorted array
# # def  remove_duplicates(arr):
# #     arr.sort()
# #     if not arr:
# #         return 0
# #     i=0
# #     for j in range(1,len(arr)):
# #         if arr[j]!=arr[i]:
# #             i+=1
# #             arr[i]=arr[j]
# #     return i+1
        

# # arr=[2,3,1,1,2,1]
# # print(remove_duplicates(arr))

# # valid palindrome

# # def valid_palindrome(s):

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
# # s="aba"
# # print(valid_palindrome(s))



# # or 


# # def valid_palindrome(s):
# #     chr=""
# #     for ch in s:
# #         if ch.isalnum():
# #             chr+=ch.lower()
# #     return ch==ch[::-1]
# # s="abagm"
# # print(valid_palindrome(s))




# # Reverse array using two pointers

# # def reverse_arr(arr):
# #     left=0
# #     right=len(arr)-1
# #     while left<=right:
# #         arr[left],arr[right]=arr[right],arr[left]
# #         left+=1
# #         right-=1
# #     return arr
# # arr=[8,7,6,5,4,3,2,1]
# # print(reverse_arr(arr))
        


# # Count pairs whose sum = target
# # def count_pairs(arr,target):
# #     res=[]
# #     count=0
# #     for i in range (len(arr)):
# #         for j in range(i+1,len(arr)):
# #             if arr[i]+arr[j]==target:
# #                 count+=1
# #                 res.append([arr[i],arr[j]])
# #                 i+=1
# #                 j+=1
# #     return count
# # arr=[1,2,3,4,5]
# # target=6
# # print(count_pairs(arr,target))
        

# # remove duplicate from sorted arr
# # def remove_dup(arr):
# #     arr.sort()
# #     if len(arr)==0:
# #         return 0
# #     i=0
# #     for j in range(1,len(arr)):
# #         if arr[j]!=arr[i]:
# #             i+=1
# #         arr[i]=arr[j]

# #     return arr[:i+1]
# # arr=[2,2,3,4,2,1,4,2]
# # print(remove_dup(arr))



# # Two sum
# def two_sum(arr,target):
#     arr.sort()
#     if len(arr)<0:
#         return 0
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         s=arr[left]+arr[right]
#         if s==target:
#             return (arr[left],arr[right])
#         if s<target:
#             left+=1
#         else:
#             right-=1
        
# arr=[2,3,2,4,5,3,8]
# target=8
# print(two_sum(arr,target))


# Remove element
def remove_ele(arr,k):
    i=0
    for num in arr:

        if num!=k:
            arr[i]=num
            i+=1

        
    return i
arr=[2,3,2,3,2]
k=2
print(remove_ele(arr,k))
            
            