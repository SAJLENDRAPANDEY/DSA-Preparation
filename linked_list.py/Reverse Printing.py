# Print the linked list in reverse order using recursion.
class node:
    def __init__(self,data):
        self.value=data
        self.next=None
def print_ll(head):
    if head is None:
        print("linked list is empty ")
    current=head
    while current is not None:
        print(current.value,end="-->")
        current=current.next
    print("None")
def reverse_print(head):
    if head is None:
        return
    reverse_print(head.next)
    print(head.value,end="-->")
head=node(10)
head.next=node(20)
head.next.next=node(30)
print_ll(head)
print(reverse_print(head))