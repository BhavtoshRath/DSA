class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

final_list = []
while a is not None:
    final_list.append(a.data)
    a = a.next

while b is not None:
    final_list.append(b.data)
    b = b.next

final_list.sort()

result = Node(-1)
temp = result
for i in range(len(final_list)):
    result.next = Node(final_list[i])
    result = result.next

dummy = Node(1)
tail = dummy

print('x')