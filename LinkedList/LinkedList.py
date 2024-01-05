class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insertAtStart(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage:
my_linked_list = LinkedList()

my_linked_list.insertAtStart(3)
my_linked_list.insertAtStart(2)
my_linked_list.insertAtStart(1)

print("Original Linked List:")
my_linked_list.print_linked_list()  # Output: 1 -> 2 -> 3 -> None

my_linked_list.reverse()

print("\nReversed Linked List:")
my_linked_list.print_linked_list()  # Output: 3 -> 2 -> 1 -> None


