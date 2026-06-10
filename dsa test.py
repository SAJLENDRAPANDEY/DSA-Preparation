# # Reverse String
# s=int(input("Enter :"))
# # def reverse_S(s):
# #     s=list(s)
# #     start=0
# #     end=len(s)-1
# #     while start<end:
# #         s[start],s[end]=s[end],s[start]
# #         start+=1
# #         end-=1
# #     return "".join(s)
# # print(reverse_S(s))

# # def reve(s):
# #     res=[]
# #     for i in range(len(s)-1,-1,-1):
# #         res.append(s[i])
# #     return "".join(res)
# # print(reve(s))

# # sentence word reverse
# # def sen(s):
# #     res=[]
# #     words=s.split()
# #     for word in words:
# #         res.append(word)
# #     res.reverse()
# #     return " ".join(res)
# # print(sen(s))


# # def sen(s):
# #     res=[]
# #     word=s.split()
# #     for i in range(len(word)-1,-1,-1):
# #         res.append(word[i])
# #     return " ".join(res)
# # print(sen(s))


# # prime number code
# def check_p(s):
#     if s<=1:
#         return False
#     for i in range(2,s):
#         if s % i==0:
#             return False
#     return True

# print(check_p(s))
        

# Palindrome
# s=input("Enter :")
# def palin(s):
#     left=0
#     right=len(s)-1
#     while left<=right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# print(palin(s))


# anagram
s=input("Enter :")
t=input("Enter :")
def chck(s,t):
    if len(s)!=len(t):
        return False
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in t:
        if ch not in freq or freq[ch]==0:
            return False
        freq[ch]-=1
    return True
print(chck(s,t))
