# linked list insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        curr = self.head

        while curr:
            print(curr.data, end="-->")
            curr = curr.next

        print("Null")

    # insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    # insert at position
    def insert_at_position(self, data, pos):
        new_node = Node(data)

        # position 0 = beginning
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head

        # reach node just before the position
        for i in range(pos - 1):

            if curr is None:
                print("Invalid Position")
                return

            curr = curr.next

        if curr is None:
            print("Invalid Position")
            return

        # insertion
        new_node.next = curr.next
        curr.next = new_node


# create linked list
l1 = LinkedList()

l1.head = Node(10)
l1.head.next = Node(20)
l1.head.next.next = Node(30)

l1.display()


# insert at beginning
l1.insert_at_beginning(5)

l1.display()


# insert at end
l1.insert_at_end(50)

l1.display()


# insert at position
l1.insert_at_position(25, 2)

l1.display()