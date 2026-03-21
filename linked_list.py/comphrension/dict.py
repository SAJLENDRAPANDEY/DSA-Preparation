# {key: value for item in iterable if condition}
# q 1 --> square of number
# x={x: x*x for x in range(1,6)}
# print(x)

# Q  2 --> Even numbers only

# x={x:x for x in range (1,8) if x%2==0}
# print(x)


# Q 3 --> odd number
# x={x:x for x in range(1,8) if x%2!=0}
# print(x)



# Q 4 --> Filter dictionary (only even keys)
# nums = {1: "one", 2: "two", 3: "three", 4: "four"}
# kv={k:v for k,v in nums.items()  if k%2==0}
# print(kv)

# Q 5 --> Change values to uppercase
# data = {1: "apple", 2: "banana"}
# x={k:v.upper() for k,v in data.items()}
# print(x)


# Q 6 --> Word & length
# words = ["apple", "banana", "kiwi"]
# wird={word:len(word) for word in words}
# print(wird)


# Q 7 --> 