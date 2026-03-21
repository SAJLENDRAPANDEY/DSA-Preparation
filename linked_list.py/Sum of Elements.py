# Find the sum of all elements in the linked list.
class node:
    def __init__(self,data):
        self.value=data
        self.next=None
def print_ll(head):
    if head is None:
        print("No element in the linked list ")
    current=head
    while current is not None:
        print(current.value,end="-->")
        current=current.next
    print("None")

def sum_of_element(head):
    if head is not None:
        print("Linked is not empty ")
    current=head
    total_sum=0
    while current is not None:
        total_sum+=current.value
        current=current.next
    return total_sum
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)
print_ll(head)
print(sum_of_element(head))


