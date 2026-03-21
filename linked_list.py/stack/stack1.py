# # # implement of stack using list
# # class Stack:
# #     def __init__(self):
# #         self.Stack=[]
# #     def push (self,val):
# #         self.Stack.append(val)
# #     def pop (self):
# #         self.Stack.pop()
# #     def peak_elemnt(self):
# #         return self.Stack[-1]
# #     def print_result(self):
# #         return self.Stack
# # s=Stack()
# # s.push(3)
# # s.push(5)
# # print(s.peak_elemnt())
# # print(s.print_result())




# #  2 implements of stack using linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def pop(self):
#         if self.head is None:
#             raise "Index error"
#         self.head=self.head.next
#     def print_data(self):
#         while self.head is not None:
#             print(self.head.data)
#             self.head=self.head.next
# s=Stack()
# s.push(4)
# s.push(7)
# print(s.print_data())
        

# Question 3 --> Check if the stack is empty or not.

# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def isEmpty(self):
#         return len(self.stack)==0
# s=stack()
# s.push(3)
# print(s.isEmpty())


# question 4 --->  Reverse a stack using another stack or recursion.
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.temp=[]
#     def push(self,val):
#         self.stack.append(val)
#     def reverse_s(self):
#         while len(self.stack)>0:
#             self.temp.append(self.stack.pop())
#         return self.temp

# s=stack()
# s.push(4)
# s.push(6)
# s.push(8)
# print(s.reverse_s())


#  question 5 --> Sort elements in a stack (smallest on top).
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def sort_top(self):
#         min_element=[-1]
#         while len(self.stack)>0:
            

# Question 6  --- > Find minimum element in stack without using sorting. 
  
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def sort_top(self):
#         min_element=self.stack[0]
#         for val in self.stack:
#             if val<min_element:
#                 min_element=val

#         return min_element
            
# s=stack()
# s.push(2)
# s.push(1)
# s.push(6)
# print(s.sort_top())



# Question 7 ---> Count Elements in Stack


# class stack:
#     def __init__(self):
#         self.stack=[]
#         count=0
#     def push(self,val):
#         self.stack.append(val)
#     def legth(self):
#         return len(self.stack)
# s=stack()
# s.push(5)
# s.push(8)
# print(s.legth())


# Question 8 -- > Display All Stack Elements 
# class stack:
#     def __init__ (self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def print_ele(self):
#         return(self.stack)
# s=stack()

# s.push(4)
# s.push(5)
# s.push(7)
# print(s.print_ele())    



# Question 9  --- > Reverse a String using Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.temp=[]
#     def push(self,s):
#         return self.stack.append(s)
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def reverse_string(self,st):
#         temp = stack()
#         for ch in st:
#             temp.push(ch)
#         reversed_string=""
#         while not temp.isEmpty():
#            reversed_string += temp.pop()

#         return reversed_string

# s=stack()
# st="hello"
# print(s.reverse_string(st))


# question 10 ---> Check Palindrome using Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def check_palindrome(self,s):


# question 11 --> Find Minimum Element in Stack 
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,x):
#         self.stack.append(x)
#     def pop(self):
#         self.stack.pop()
    
#     def min_ele(self):
#         min_ele=self.stack[0]
#         for val in self.stack:
#             if val < min_ele:
#                 min_ele=val
#         return min_ele
# s=stack()
# s.push(2)
# s.push(0)
# s.push(6)
# s.push(8)
# print(s.min_ele())
        

# Question 11 --> Check if Stack is Full (Fixed Size Stack) 
# class stack:
#     def __init__(self,capacity):
#         self.stack=[]
#         self.capacity=capacity
#     def isFull(self):
#         return len(self.stack)==self.capacity
#     def push(self,val):
#         if self.isFull():
#             return "Stack overflow"
#         self.stack.append(val)
# s=stack(5)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# print(s.isFull())
# s.push(6)
# s.push(7)
# print(s.push(7))


# Question 11 --> Delete Middle Element of Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def middle(self):
#         n=len(self.stack)//2
#         temp=[]
#         for _ in range(n):
#             temp.append(self.pop())
#         self.pop()
#         while temp:
#             self.push(temp.pop())

        
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.middle()
# print(s.stack)


# Question 12 ---> Duplicate Top Element
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def is_empty(self):
#         return len(self.stack)==0
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         return self.stack[-1]
#     def duplictes(self):
#         if self.is_empty():
#             return "No element in stack"
#         top=self.peek()
#         self.push(top)
# s=stack()
# s.push(4)
# s.push(6)
# s.push(7)
# s.push(8)
# s.duplictes()
# print(s.stack)



# Question 13 --> Swap Top Two Elements
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         self.stack.pop()
#     def peek(self):
#         return self.stack[-1]
#     def swap_t(self):
#         if len(self.stack)==0:
#             return "stack is empty"
#         self.stack[-1],self.stack[-2]=self.stack[-2],self.stack[-1]
#         return self.stack
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# print("original stack",s.stack)
# s.swap_t()
# print(s.stack)


# question 14 --> Sum of All Stack Elements
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def is_empty(self):
#         return len(self.stack)==0
#     def sum_ele(self):
#         temp=[]
#         while not self.is_empty():
#             temp.append(self.stack.pop())
#         return sum(temp)
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# print(s.sum_ele())

# Question 15 -->  Check Even or Odd Count of Elements
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def isEmpty(self):
#         return len(self.stack)==0
#     def check_even(self):
#         while not self.isEmpty():
#             if len(self.stack)%2==0:
#                 return "Even"
#             else:
#                 return "odd"
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# print(s.check_even())


# Question 16 --> Reverse Stack Elements using Another Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def isempty(self):
#         return len(self.stack)==0
#     def reverse_stack(self):
#         temp=[]
#         while not self.isempty():
#             temp.append(self.pop())
#         return temp
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# print(s.stack)


# print(s.reverse_stack())

# Question 17 --->Sort Stack (Smallest on Top)
 
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def isempty(self):
#         return len(self.stack)==0
#     def peek(self):
#         return self.stack[-1]
#     def sort_stack(self):
#         temp=[]
#         while not self.isempty():
#             curr=self.pop()
#             while temp and temp[-1]>curr:
#                 self.push(temp.pop())
#             temp.append(curr)
            
#         return temp
# s=stack()
# s.push(2)
# s.push(3)
# s.push(1)
# s.push(5)
# print(s.sort_stack())


# Question 18 --> Push Only Even Numbers 
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def push_even(self,val):
#         if val%2==0:
#             return self.stack.append(val)
# s=stack()
# s.push_even(2)
# s.push_even(3)
# s.push_even(4)
# s.push_even(6)
# s.push_even(7)
# print(s.stack)


# Question 19 --> Pop Until Stack Becomes Empty
# class stack:
#     def __init__(self,capacity):
#         self.stack=[]
#         self.capacity=capacity
#     def push(self,val):
#         self.stack.append(val)
#     def isEmpty(self):
#         return len(self.stack)==0
#     def isfull(self):
#         if len(self.stack)==self.capacity:
#             return "stack is full"
#         else:
#             return "Empty"
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty!"
#         else:
#             self.stack.pop()
#             if self.isEmpty():
#                 return "stack is now empty "
#             else:
#                 return "element popped "
        
            
        
    
#     def peek(self):
#         return self.stack[-1]
    
# s=stack(2)
# s.push(2)
# s.push(3)
# # s.push(4)
# s.pop()
# print(s.pop())
# print(s.pop())
# print(s.pop())



# Question 20 --> Check if Top Element is Even or Odd 
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def peek(self):
#         return self.stack[-1]
#     def check_even(self):
#         if self.peek()%2==0:
#             return "Even"
#         else:
#             return "odd"
# s=stack()
# s.push(3)
# s.push(3)
# s.push(4)
# print(s.check_even())


# Question 21 --> Push Characters of Your Name
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def print_s(self):
#         return (self.stack)
# s=stack()
# s.push("y")
# s.push("a")
# s.push("s")
# s.push("h")
# print(s.print_s())


# or 


# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
# s=stack()
# name="YASH"
# for ch in name:
#     s.push(ch)
# print(s.stack)


# Question 22 --> Push Only Strings not any integer
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
# s=stack()
# items=[10,"string",20,"yash",40.0]
# for char in items:
#     if isinstance(char,str):
#         s.push(char)

# print(s.stack)


# Question 23 --> Check If Stack Contains a Specific Value
# class stack:
#     def __init__(self):

#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def search(self,val):
#         for element in self.stack:
#             if element==val:
#                 return "Value Found"
        
#         return "not found"
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(6)
# print(s.search(3))
        


# question 23 --> Count Only Odd Numbers in Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def count_odd(self):
#         count=0
        
#         for val in self.stack:
#             if val%2!=0:
#                 count+=1
#         return count
# s=stack()
# s.push(2)
# s.push(3)
# s.push(5)
# s.push(6)
# print(s.count_odd())


# Question 24 --> Push Fruits into Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         return self.stack.append(val)
#     def peek(self):
#         return self.stack[-1]
#     def pop(self):
#         self.stack.pop()
# s=stack()
# s.push("mango")
# s.push("apple")
# s.push("banana")
# print(s.peek())



# Question 25 --> Remove All Elements Greater Than 10
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         for val in self.stack:
#             if val<10:
#                 return self.stack.pop()
# s=stack()
# s.push(2)
# s.push(3)
# s.push(11)
# s.push(33)
# s.push(44)
# s.pop()
# s.pop()
# s.pop()
# print(s.stack)

# Question 26 --> Push 5 Numbers and Print Only the Middle One
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def middle(self):
#         n=len(self.stack)//2
#         return self.stack[n]
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.middle())

# Question 27 --> Copy One Stack to Another
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def isEmpty(self):
#         return len(self.stack)==0
#     def copy_stack(orginal):
#         temp=stack()
#         copy=stack()
#         while not orginal.isEmpty():
#             temp.push(orginal.pop())
#         while not temp.isEmpty():
#             val=temp.pop()
#             orginal.push(val)
#             copy.push(val)
#         return copy
# s=stack()
# s.push(2)
# s.push(3)
# s.push(4)

# s1=s.copy_stack()


# print("Original Stack:", s.stack)
# print("Copied Stack:  ", s1.stack)



# Question 28 ---> Multiply All Elements in Stack
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         return self.stack.pop()
#     def multiply_all(self):
#         result = 1
#         temp = []

#         # Pop all elements and multiply
#         while self.stack:
#             val = self.pop()
#             result *= val
#             temp.append(val)

#         # Push elements back (to restore original stack)
#         while temp:
#             self.push(temp.pop())

#         return result
# s=stack()
# s.push(2)
# s.push(4)
# s.push(5)
# print(s.multiply_all())