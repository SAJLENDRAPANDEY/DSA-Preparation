# # Basic Stack
# stack=[]
# stack.append(10)
# stack.append(20)

# # stack.pop()




# print(stack)


# Question 1 --> String ko reverse karo using stack
def reverse_string(s):
    stack=[]
    for ch in s:
        stack.append(ch)
    res=""
    while stack:
        res+=(stack.pop())
    return res
print(reverse_string("Hello"))