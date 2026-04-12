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
# def  reverse_String(s):
#     result=" "
#     for i in range(len(s)-1,-1,-1):
#         result+=s[i]
#     return result
    
# s="hello"
# print(reverse_String(s))


# Q 4 --> Palindrome check
# def palindrome_check(s):
#     s=s.lower().replace(" ","")
#     return s==s[::-1]
# s="madamg"
# print(palindrome_check(s))


#  or 
# def palindrome_check(s):
#     start=0
#     stop=len(s)-1
#     while start<stop:
#         if s[start]!=s[stop]:
#             return False
#         start+=1
#         stop-=1
#     return True
# s="madam"
# print(palindrome_check(s))


# Q 5 --> Count characters
# def count_char(s):
#     freq={}
#     for ch in s:
#         freq[ch]=freq.get(ch,0)+1
#     return freq
# s="hello"
# print(count_char(s))



# Q 6 -->> Remove spaces
# def remove_space(s):
#     return (s.replace(" ",""))
# s="hello World"
# print(remove_space(s))


# Q 7-->First non-repeating character
def check_repeating(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in freq:
        if freq[ch]==1:
            return ch
s="aabbcdd"
print(check_repeating(s))
