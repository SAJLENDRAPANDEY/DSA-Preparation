# # # Reverse String
# # s=int(input("Enter :"))
# # # def reverse_S(s):
# # #     s=list(s)
# # #     start=0
# # #     end=len(s)-1
# # #     while start<end:
# # #         s[start],s[end]=s[end],s[start]
# # #         start+=1
# # #         end-=1
# # #     return "".join(s)
# # # print(reverse_S(s))

# # # def reve(s):
# # #     res=[]
# # #     for i in range(len(s)-1,-1,-1):
# # #         res.append(s[i])
# # #     return "".join(res)
# # # print(reve(s))

# # # sentence word reverse
# # # def sen(s):
# # #     res=[]
# # #     words=s.split()
# # #     for word in words:
# # #         res.append(word)
# # #     res.reverse()
# # #     return " ".join(res)
# # # print(sen(s))


# # # def sen(s):
# # #     res=[]
# # #     word=s.split()
# # #     for i in range(len(word)-1,-1,-1):
# # #         res.append(word[i])
# # #     return " ".join(res)
# # # print(sen(s))


# # # prime number code
# # def check_p(s):
# #     if s<=1:
# #         return False
# #     for i in range(2,s):
# #         if s % i==0:
# #             return False
# #     return True

# # print(check_p(s))
        

# # Palindrome
# # s=input("Enter :")
# # def palin(s):
# #     left=0
# #     right=len(s)-1
# #     while left<=right:
# #         if s[left]!=s[right]:
# #             return False
# #         left+=1
# #         right-=1
# #     return True
# # print(palin(s))


# # anagram
# # s=input("Enter :")
# # t=input("Enter :")
# # def chck(s,t):
# #     if len(s)!=len(t):
# #         return False
# #     freq={}
# #     for ch in s:
# #         freq[ch]=freq.get(ch,0)+1
# #     for ch in t:
# #         if ch not in freq or freq[ch]==0:
# #             return False
# #         freq[ch]-=1
# #     return True
# # print(chck(s,t))


# # Largest Element
# # def check_m(arr):
# #     mx=0
# #     for num in arr:
# #         if num>mx:
# #             mx=num
# #     return mx
# # arr=[2,3,1,9]
# # print(check_m(arr))


# # # Second highest number
# # def check_h(arr):
# #     largest=float("-inf")
# #     sec=float("-inf")
# #     for num in arr:
# #         if num>largest:
# #             sec=largest
# #             largest=num
# #         elif num>sec  and num!=largest:
# #             sec=num
# #     return sec
# # arr=[9,3,2,1]
# # print(check_h(arr))
        

# # # count vowels
# # s=input("Enter :")
# # def count_v(s):
# #     count=0
# #     vowels="aeiouAEIOU"
# #     for ch in s:
# #         if ch in  vowels:
# #             count+=1
# #     return count
# # print(count_v(s))

# # Frequency of Characters
# # s=input("Enter : ")
# # def check_F(s):
# #     freq={}
# #     for ch in s:
# #         freq[ch]=freq.get(ch,0)+1
# #     return freq
# # print(check_F(s))


# # Two Sum
# # def two_sum(arr,target):
# #     left=0
# #     right=len(arr)-1
# #     while left<right:
# #         s=arr[left]+arr[right]
        
# #         if s==target:
# #             return True
# #         elif s<target:
# #             left+=1
# #         else:
# #             right-=1
# #     return False

# # arr = [2,7,11,15]
# # target = 97
# # print(two_sum(arr,target))


# # Remove Duplicates
# # def remo_l(arr):
# #     j=0
# #     for i in range(1,len(arr)):
# #         if arr[i]!=arr[j]:
# #             j+=1
# #             arr[j]=arr[i]
# #     return arr[:j+1]
# # arr=[2,2,3,4,5]
# # print(remo_l(arr))



# # def rem_l(arr):
# #     seen={}
# #     res=[]
# #     for num in arr:
# #         if num not in res:
# #             res.append(num)
# #     return res
# # arr=[2,2,4,2,5]
# # print(rem_l(arr))
            


# # Binary Search
# def bina(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         s=left+right//2
#         if arr[s]==target:
#             return True
#         elif arr[s]<target:
#             left=s+1
#         else:
#             right=s-1
#     return False
# arr=[2,3,4,5]
# print(bina(arr,target=57))


# fibonnaci
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-2) +fibo(n-1)
print(fibo(4))