# # # Find the maximum element in the linked list.
# # class node:
# #     def __init__(self,data):
# #         self.value=data
# #         self.next=None
# # def print_ll(head):
# #     if head is None:
# #         print("linked list is empty ")
# #     current=head
# #     while current is not None:
# #         print(current.value,end="-->")
# #         current=current.next
# #     print("None")
# # def max(head):
# #     current=head
# #     max=0
# #     res=[]
   
# #     if head is None:
# #         print("ll is empty ")
# #         return None
# #     max_value=head.value
# #     current=head
# #     while current is not None:
# #         if current.value>max_value:
# #             max_value=current.value
# #         current=current.next
# #     return max_value
# # head=node(10)
# # head.next=node(20)
# # head.next.next=node(30)
# # head.next.next.next=node(40)
# # print_ll(head)
# # print(max(head))


        

# #       min     
# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     if head is None:
#         print("linked is empty ")
#     current=head
#     while current is not None:
#         print(current.value,end="-->")
#         current=current.next
#     print("None")
# def min(head):
#     if head is None:
#         print("Linked is empty ")
#     current=head
#     max_value=current.value
#     while current is not None:
#         if current.value<max_value:
#             max_value=current.value
#         current=current.next
#     return max_value
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# print_ll(head)
# print(min(head))    




