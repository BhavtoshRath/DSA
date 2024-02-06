# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head): # Time complexity: O(N), Space complexity: O(1)
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
original_head = ListNode(1)
original_head.next = ListNode(2)
original_head.next.next = ListNode(3)
original_head.next.next.next = ListNode(4)
original_head.next.next.next.next = ListNode(5)

# Reverse the linked list
reversed_head = reverseLinkedList(original_head)

# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
current = reversed_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")