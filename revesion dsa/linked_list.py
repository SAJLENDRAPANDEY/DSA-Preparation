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


# insert at beginging
new_node=Node(5)
# new_node.next=l1.head
# l1.head=new_node

# l1.display()


# insert at the end
curr=l1.head
while curr.next is not None:
    curr=curr.next
curr.next=Node(50)
l1.display()
