# # Count nodes
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def print_ll(head):
#     if head is None:
#         print("Linked list is empty")
#     current=head
#     while current is not None:
#         print(current.data,end="-->")
#         current=current.next
#     print("None")
# def insert_at_end(head,data):
#     new_node=node(data)
#     if head is None:
#         return new_node
#     current=head
#     while current.next is not None:
#         current=current.next
#     current.next=new_node
#     return head

# def count_node(head):
#     count=0
    
#     current=head
#     while  current is not None:
#         count+=1
#         current=current.next
#     return count
# head=node(10)
# head=insert_at_end(head,20)
# head=insert_at_end(head,30)
# head=insert_at_end(head,40)
# print_ll(head)
# print("Count nodes",count_node(head))






# # head=node(10)
# # head.next=node(20)
# # head.next.next=node(30)
# # head.next.next.next=node(40)
# # print_ll(head)

