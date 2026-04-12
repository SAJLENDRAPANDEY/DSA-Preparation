# #  Q 1 --> Count vowels
# def count_vowels(s):
#     vowel=set("aeiouAEIOU")
#     count=0
#     for ch in s:
#         if ch in vowel:
#             count+=1
        
#     return count
# s="hello"
# print(count_vowels(s))


# Q 2 --> Reverse string
# def reverse_string(s):
#     s=list(s)
   
#     start=0
#     stop=len(s)-1
#     while start<=stop:
#         s[start],s[stop]=s[stop],s[start]
#         start+=1
#         stop-=1

#     return ''.join(s)
# s="hello"
# print(reverse_string(s))

# or 
def  reverse_String(s):
    result=" "
    for i in range(len(s)-1,-1,-1):
        result+=s[i]
    return result
    
s="hello"
print(reverse_String(s))