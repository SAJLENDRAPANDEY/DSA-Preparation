# # Palindrome
# def is_palindrome(s):
#     left=0
#     right=len(s)-1
#     while left<=right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# s="abac"
# print(is_palindrome(s))

# Q 2-->Reverse string
# def reverse_string(s):
#     s=list(s)
#     left=0
#     right=len(s)-1
#     while left<=right:
#         s[right],s[left]=s[left],s[right]
#         left+=1
#         right-=1
#     return "".join(s)
# s="abc"
# print(reverse_string(s))


# Q 3 --> Remove duplicates
def remove_duplicate(s):
    s=list(s)
    slow=0
    for fast in range(len(s)):
        if s[fast]!=s[slow]:
            slow+=1
            s[slow]=s[fast]
    return "".join(s[:slow+1])
s="abbaaa"
print(remove_duplicate(s))
            
