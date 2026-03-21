# create a linked l
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linked_list:
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return 
#         last=self.head
#         while last.next:
#             last=last.next
#         last.next=new_node
#     def print_list(self):
#         temp=self.head
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# ll=linked_list()
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(6)
# print(ll.print_list())
    
        

# q 1 --> Insert a node at the beginning of the linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.data=None
    def append(self,data):
        self.data=data
        new_node=Node(data)
        while self.head is None:
            self.head=new_node
            return 

    

    
    