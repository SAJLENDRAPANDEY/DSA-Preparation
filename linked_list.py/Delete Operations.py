# # # # Delete the first node of the linked list
# # # class node:
# # #     def __init__(self,data):
# # #         self.value=data
# # #         self.next=None
# # # def print_ll(head):
# # #     currrent=head
# # #     while currrent.next is not None:
# # #         print(currrent.value,end="-->")
# # #         currrent=currrent.next

# # # def delete_first_node(head):
# # #     if head is None:
# # #         print("linked list is empty")
# # #         return None
# # #     return head.next



# # # def insert_at_end(self,head,data):
# # #     new_node=node(data)
# # #     if head is None:
# # #         return head
# # #     current=head
# # #     while current.next is not None:
# # #         currrent=current.next
# # #     currrent.next=new_node
# # #     return head
# # # head=node(10)
# # # head.next=node(20)
# # # head.next.next=node(30)
# # # head.next.next.next=node(40)
# # # print("Original linked list ")
# # # print(print_ll(head))
# # # head=delete_first_node(head)
# # # print_ll(head)
    



# # # q2--> Delete the last node of the linked list.
# # class node:
# #     def __init__(self,data):
# #         self.value=data
# #         self.next=None
# # def print_ll(head):
# #     if head is None:
# #         return
# #     current=head
# #     while current.next is not None:
# #         print(current.value,end="-->")
# #         current=current.next
# # def insert_at_beginning(self,head,data):
# #     new_node=node(data)
# #     new_node.next=head
# #     return new_node
# # def delete_at_end(head):
# #     if head is None:
# #         print("no element in the ll")
# #     current=head
# #     while current.next.next is not None:
# #         current=current.next
# #     current.next=None
# #     return head







# # head=node(10)
# # head.next=node(20)
# # head.next.next=node(30)
# # head.next.next.next=node(40)
# # print("Original linked list")
# # print(print_ll(head))

# # head=delete_at_end(head)
# # print(print_ll(head))


# # delete at specific position
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     current=head
#     while current.next is not None:
#         print(current.value,end="-->")
#         current=current.next
# def insert_at_end(head,data):
#     new_node=node(data)
#     if head is None:
#         head=new_node
#         # return head
#     current=head
#     while current is not None:
#         current=current.next
#     current.next=new_node
#     return head

# def delete_at_specific(head,pos):
    
#     if pos==1:
#         return head.next
#     current=head
#     count=1
#     while current is not None and count<pos-1:
#         current=current.next
#         count+=1
#     if current is None or current.next is None:
#         print("position is out of range ")
#         return head
#     current.next=current.next.next
#     return head
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# print("Original linked list ")
# print(print_ll(head))
# head=delete_at_specific(head,2)
# print("delete linked list ")
# print(print_ll(head))








# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)



    