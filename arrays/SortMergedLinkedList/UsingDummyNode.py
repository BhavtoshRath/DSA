class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)  # a = 1->3->5->None

b = Node(2)
b.next = Node(4) # b = 2->4->None


def UsingDummyNode(l1, l2):
    dummy = Node()
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            tail.next = l1   # .next = -> Drawn the pointer
            l1 = l1.next # l1 = -> Update the pointer name
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1 is not None:
        tail.next = l1
    if l2 is not None:
        tail.next = l2

    return dummy.next

dummy = UsingDummyNode(a, b)
print(UsingDummyNode(a, b))