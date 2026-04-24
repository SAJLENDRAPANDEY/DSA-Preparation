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
# def remove_duplicate(s):
#     s=list(s)
#     slow=0
#     for fast in range(len(s)):
#         if s[fast]!=s[slow]:
#             slow+=1
#             s[slow]=s[fast]
#     return "".join(s[:slow+1])
# s="abbaaa"
# print(remove_duplicate(s))
            


# Remove duplicates
# def remove_dup(s):
#     s=list(s)
#     slow=0
#     for fast in range(len(s)):
#         if s[fast]!=s[slow]:
#             slow+=1
#             s[slow]=s[fast]
#     return "".join(s[:slow+1])
# s="AAAAABBBFSSDSA"
# print(remove_dup(s))


# leetcode(1768) Merge alternatively
# def mergeAlternately(word1, word2):
#     res=[]
#     i=0
#     j=0
#     while i<len(word1) or j<len(word2):
#         if i<len(word1):
#             res.append(word1[i])
#             i+=1
#         if j<len(word2):
#             res.append(word2[j])
#             j+=1
#     return "".join(res)
# word1="ace"
# word2="bdf"
# print(mergeAlternately(word1,word2))



# valid palindrome
# def palimdrome(s):
#     left=0
#     right=len(s)-1
#     while left<=right:
#         if not s[left].isalnum():
#             left+=1
#             continue
#         if not s[right].isalnum():
#             right-=1
#             continue
#         elif s[left].lower()!=s[right].lower():
#             return False
#         left+=1
#         right-=1

#     return True
# s="Abc 012..##  10cb9A"
# print(palimdrome(s))



# Reverse String
# def reverseString(s: str) -> str:
#         # code here
#         s=list(s)
#         left=0
#         right=len(s)-1
#         while left<=right:
#             s[left],s[right]=s[right],s[left]
#             left+=1
#             right-=1
#         return "".join(s)
# s="abc"
# print(reverseString(s))



# Reverse Words(gfg)
# def reverseWords(s):
#         # code here
#         word=s.split(".")
#         word=[w for w in word if w!=""]
#         left=0
#         right=len(word)-1
#         while left<right:
#             word[left],word[right]=word[right],word[left]
#             left+=1
#             right-=1
#         return ".".join(word)
# s = "i.like.this.program.very.much"
# print(reverseWords(s))



# Remove duplicates
def removeDuplicates(s):
    res = []
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in freq:   # correct indentation
        if freq[ch] == 1:
            res.append(ch)
    
    return "".join(res)


s = "AAbbbaaaccd"
print(removeDuplicates(s))
