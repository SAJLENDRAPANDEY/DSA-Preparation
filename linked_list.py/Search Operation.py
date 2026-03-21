# # Search if a given value exists in the linked list or not.

# class node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
# def print_ll(head):
#     if head is None:
#         print("No element in the ll")
#         return 
#     current=head
#     while current is not None:
#         print(current.value,end="-->")
#         current=current.next
# def insert_at_end(head,data):
#     new_node=node(data)
#     if head is None:
#         return new_node
#     current=head
#     while current.next is not None:
#         current=current.next
#     current.next=new_node
#     return head
# def search_element(head,target):
    
#     current=head
#     while current is not None:
#         if current.value==target:
#             print("element is found",target)
#             return True
        
#         current=current.next
#     print("Element is not founnd in ll")
#     return False




# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# print_ll(head)


# found=search_element(head,20)
# print("Element found",found)
    