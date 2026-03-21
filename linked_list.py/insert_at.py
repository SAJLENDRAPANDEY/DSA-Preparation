# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     current=head
#     while current is not None:
#         print(current.value,end="-> ")
#         current=current.next
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# # l=node(head)
# print(print_ll(head))

# q1 --> insert at beginning
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     current=head
#     while current is not None:
#         print(current.value,end="->")
#         current=current.next

# def insert_at_beginning(head,data):
#     new_node=node(data)
#     new_node.next=head
#     return new_node
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# print("original linked list ")
# print(print_ll(head))

# head=insert_at_beginning(head,5)
# print("After insert at beginning ")
# print(print_ll(head))
        

# q2 --> insert at specific position 
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     current=head
#     while current is not None:
#         print(current.value,end=" -> ")
#         current=current.next
#     print("none")
# def insert_at_end(head,data):
#     new_node=node(data)
#     if head is None:
#         return new_node
#     current=head
#     while current.next is not None:
#         current=current.next
#     current.next=new_node
#     return head
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# print(" original  linked list ")
# print(print_ll(head))

# head=insert_at_end(head,50)
# print(print_ll(head))




# q 3  --> insert at the end
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None

# def print_ll(head):
#     current=head
#     while current.next is not None:
#         print(current.value,end="->")
#         current=current.next
#     print("None")
# def insert_at_end(head,data):
#     new_node=node(data)
#     while head is None:
#         return new_node
#     current=head
#     while current.next is not None:
#         current=current.next
#     current.next=new_node
#     return head
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# print("original ll")
# print(print_ll(head))
# head=insert_at_end(head,40)
# print(print_ll(head))


    
# Q4 --> insert at specific position
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     current=head
#     while current.next is not None:
#         print(current.value,end="-->")
#         current=current.next
# def insert_at_position(head,data,pos):
#     new_node=node(data)
    
#     if pos==1:
#         head=new_node
#         return head
#     current=head
#     count=1
#     while current is not None and count < pos-1:
#         current=current.next
#         count+=1
#     if current is None:
#         print("Position out of range, inserting at end")
#         return head
#     new_node.next=current.next
#     current.next=new_node
#     return head
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# print("Original linked list")
# print(print_ll(head))

# head=insert_at_position(head,15,2)

# print(print_ll(head))

