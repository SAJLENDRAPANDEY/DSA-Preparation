# # Q1. Implement Stack using Array
# class Stack():
#     stack=[]
#     def push(self):
#         element=int(input("Enter the number :"))
#         self.stack.append(element)
#         print("Element push to stack is :",element)

#     def pop(self):
#         if not self.stack:
#             print("Stack is Empty ")
#             return
#         ele=self.stack.pop()
#         print("Element pop:",ele)
#     def peek(self):
#         if not self.stack:
#             print("Stack is Empty")
#             return
#         ele=self.stack[-1]
#         print("Top element is :",ele)

#     def isempty(self):
#         if len(self.stack)==0:
#             print("Stack is  empty")


# s=Stack()
# s.push()
# s.push()

# print(s.stack)

# s.pop()
# print(s.stack)

# s.peek()
# print(s.stack)

# s.isempty()
# print(s.stack)









# Q 2. Implement Stack using Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self):
        ele=int(input("Enter number :"))
        new_node=Node(ele)
        new_node.next=self.top
        self.top=new_node

        print("Element add successfully :",ele)

    def pop(self):
        if self.top is None:
            print("Stack is None")
            return 
        ele=self.top.data
        self.top=self.top.next

        print("Element pop:",ele)
s=Stack()
s.push()

s.pop()
# print(s.push)

    