# Q1. Implement Stack using Array
class Stack():
    stack=[]
    def push(self):
        element=int(input("Enter the number :"))
        self.stack.append(element)
        print("Element push to stack is :",element)
s=Stack()
s.push()
print(s.stack)