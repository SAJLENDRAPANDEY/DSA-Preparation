# # Square of numbers

# square=[x*x  for x in range(1,6)]
# print(square)


# #  q 2 --> Only even numbers
# even=[x for x in range(1,10) if x%2==0]
# print(even)


#  q 3 --> only odd numbers
# odd=[x for x in range(1,10) if x%2!=0]
# print(odd)

#  q 4 --> Uppercase words
# x=["ood","apple"]
# upper=[x.upper() for x in x ]
# print(upper)


# q 5 ---> if–else in List Comprehension
# x=["even" if x %2==0 else "odd" for x in range(1,10)]
# print(x)

#  q 6 --> Positive or Negative
# nums = [-3, -1, 0, 2, 5]
# x=["positive" if x>0 else "negative" for x in nums]
# print(x)

# Q 7 --> Words starting with 'a'
# words = ["apple", "ball", "ant", "cat"]
# a_words=[word for word in words if word.startswith("a")]
# a_words=[word for word in words if word.endswith("t")]
# print(a_words)


# Q 8 --> Remove vowels
# text="yash"
# char=[char for char in text if char not in "aeiou"]
# print(char)

