#  Q 1 --> Count vowels
def count_vowels(s):
    vowel="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowel:
            count+=1
        else:
            count=1
    return count
s="hello"
print(count_vowels(s))