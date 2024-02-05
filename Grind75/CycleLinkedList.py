# https://leetcode.com/problems/linked-list-cycle/description/
# Using Floyd's Tortoise and Hare algorithm.


class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def hascycle(root):  # Time complexity: O(N), Space complexity: O(1)
    if root is None or root.next is None:  # Base case. If LL is empty or 1 node
        return False
    slow = root.next
    fast = root.next.next
    while slow != fast:
        if fast is None or fast.next is None:  # Cycle list can never end with None.
            return False
        else:
            slow = slow.next  # Tortoise
            fast = fast.next.next  # Hare
    return True
