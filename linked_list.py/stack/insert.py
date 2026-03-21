# # Implement a stack using a list or linked list and perform push(), pop(), and peek() operations.

# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         return self.stack[-1]
#     def print_data(self):
#         return self.stack

# s=stack()
# s.push(3)
# s.push(5)
# # s.pop()
# print(s.peek())
# print(s.print_data())

# #  question 2 --->  Write a function isEmpty() that returns True if the stack is empty, else False.

# class stack:
#     def __init__(self):
#         self.stack=[]

#     def push(self,val):
#         self.stack.append(val)
        
#     def check_isempty(self):
#         return len(self.stack)==0
# s=stack()
# s.push(6)
# print(s.check_isempty())


# Question 3 ---> Count and return the number of elements currently in the stack.
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.count=0
#     def push(self,val):
#         return self.stack.append(val)
#     def return_leno(self):
#         return len(self.stack)
# s=stack()
# s.push(5)
# s.push(6)
# s.push(8)
# s.push(9)
# s.push(2)
# print(s.return_leno())
    


#  question 4 Reverse the elements of a given stack using another stack or recursion.
# def reverse_stack(stack):
#     temp_stack=[]
#     while len(stack) > 0:
#         temp_stack.append(stack.pop())
    
#     return temp_stack
# stack=[1,3,4,5,6,8]
# print(reverse_stack(stack))


# Question 5 ---> Write a function to get the minimum element from the stack without using sorting.

# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         return self.stack.append(val)
#     def is_empty(self):
#         return len(self.stack)==0
#     def min_element(self):

#         min_element=self.stack[-1]
#         temp_stack=[]
#         while not self.is_empty():
#             top=self.pop()
#             if top<min_element:
#                 min_element=top
#             temp_stack.append(top)
#         while len(temp_stack) > 0:
#             self.push(temp_stack.pop())
#         return min_element

#         # return (min(self.stack()))
# s=Stack()
# s.push(4)
# s.push(2)
# s.push(7)
# print(s.min_element())



# q 5  --- > Check if a string of brackets ()[]{} is balanced or not. 
class stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    s="()[]{}"
    def check(self):
        