class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(20)

print(a)