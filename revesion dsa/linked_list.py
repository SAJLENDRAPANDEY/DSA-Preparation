# linked list insertion
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end="-->")
            curr=curr.next
        print("Null")
l1=LinkedList()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.display()