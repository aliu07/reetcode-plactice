from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Intuition:
        We iterate through the list 2 nodes at a time. Then, we just
        need to perform some pointer manipulation.

        Note the creation of a dummy node to be able to return the head
        at the end.

    Runtime:
        O(n) since we need 1 pass on the linked list.

    Memory:
        O(1) since we are only performing pointer manipulations.
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev, ptr = dummy, head

        while ptr and ptr.next:
            adj = ptr.next

            # Rearrange pointers
            prev.next = adj
            ptr.next = adj.next
            adj.next = ptr

            # Increment prev & ptr pointers
            prev = ptr
            ptr = ptr.next

        return dummy.next
