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
# stack=[2]
# def check_empty(stack):
#     return len(stack)==0
        
    
# print(check_empty(stack))



# Question 3 -> Print Stack in Reverse
# def reverse_s(s):

#     stack=[]
#     for ch in s:
#         stack.append(ch)
#     while stack:
#         print(stack.pop(),end=",")
        
# reverse_s("123")


# Queston 4 --> check len of stack withought using len function
# def len_Stack(s):
#     count=0
#     while s:
#         s.pop()
#         count+=1
#     return count
# s=[]
# print(len_Stack(s))



# Question 5 ----->  Stack me max element find karo

# def max_ele(stack):
#     max=0
#     while stack:
#         if stack.pop>max:
#             max=stack.pop

#     return max
# max_ele(stack=[2,34,5])




# q 6 -> Stack me max element find karo
# def max_stack(stack):
#     if len(stack)==1:
#         return stack[0]
#     max_e=stack[0]
#     while stack:
#         value=stack.pop()
#         if value>max_e:
#             max_e=value
        
#     return max_e
# stack=[2,3,6,4]
# print(max_stack(stack))


# q 7 --> Stack copy karo (new stack banao)
# def stack(s):
#     st=[]
#     while s:
#        st.append(s.pop())
#     st.reverse()
#     return st
# s=[1,2,3]
# print(stack(s))


# Q 8 --> Stack ko empty karo
# def stack_e(s):
#     while s:
#         s.pop()
#     return len(s)
# s=[1,2,3,4]
# print(stack_e(s))


# Q 9 --> Count even numbers in stack
# def count_even(s):
#     count=0
#     while s:
#         value=s.pop()
#         if value%2==0:
#             count+=1
#     return count
# s=[1,2,3,4,6]
# print(count_even(s))



# Q 10 --> Top 2 elements ka sum print karo
def stack_t(s):
    
    v=s.pop()
    v2=s.pop()
    return v+v2
s=[1,2,3,4]
print(stack_t(s))
