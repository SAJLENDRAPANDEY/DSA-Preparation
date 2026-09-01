# Q1. Implement Stack using Array
class Stack():
    stack=[]
    def push(self):
        element=int(input("Enter the number :"))
        self.stack.append(element)
        print("Element push to stack is :",element)

    def pop(self):
        if not self.stack:
            print("Stack is Empty ")
            return
        ele=self.stack.pop()
        print("Element pop:",ele)


s=Stack()
s.push()

print(s.stack)

s.pop()
print(s.stack)