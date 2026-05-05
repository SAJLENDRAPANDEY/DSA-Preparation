# # Basic Stack
# stack=[]
# stack.append(10)
# stack.append(20)

# # stack.pop()




# print(stack)


# Question 1 --> String ko reverse karo using stack
# def reverse_string(s):
#     stack=[]
#     for ch in s:
#         stack.append(ch)
#     res=""
#     while stack:
#         res+=(stack.pop())
#     return res
# print(reverse_string("Hello"))


# Question 2 --> Check stack empty or not
stack=[2]
def check_empty(stack):
    return len(stack)==0
        
    
print(check_empty(stack))