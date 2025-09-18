from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Intuition:
        Use 2 pointers, 1 travels fast (jump 2 nodes per iter), the
        other travels slow (only jumps 1 node per iter). If ever they
        meet, that means we have a cycle. Otherwise, if one reaches
        the end of the linked list, then we know we do not have any
        cycles.

    Runtime:
        O(n) since we need to traverse the linked list

    Memory:
        O(1) since we are only storing pointers
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
