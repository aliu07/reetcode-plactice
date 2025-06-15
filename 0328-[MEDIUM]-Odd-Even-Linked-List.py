from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Intuition:
        We use 2 pointers to iterate through odd and even nodes separately.
        We also need to store a pointer to the head of the odd and even linked
        lists.

        The trickiest part for me was determining the loop condition for the
        while block. However, after some thought, you realize that even is
        the rightmost pointer at any moment in the list (i.e. nearest to the
        end). Therefore, we just iterate until we exast the next even node.

    Runtime:
        O(n) -> one pass

    Memory:
        O(1) -> only using pointers and rearranging existing pointers
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Store pointer to head of each linked list
        oddHead, evenHead = head, head.next
        # Use ptrs to iterate
        oddCurr, evenCurr = head, head.next

        while evenCurr and evenCurr.next:
            # Save previous node temporarily
            oddTmp = oddCurr
            # Shift current ptr to next odd node
            oddCurr = oddCurr.next.next
            # Link previous odd node to new current odd node
            oddTmp.next = oddCurr

            # Same thing for even nodes
            evenTmp = evenCurr
            evenCurr = evenCurr.next.next
            evenTmp.next = evenCurr

        # Link both lists
        oddCurr.next = evenHead

        return oddHead
