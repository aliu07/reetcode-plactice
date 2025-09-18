from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        We store the current node and the previous node at every
        step. Initially, the previous node is set to None. In the
        loop, we store the next node in a tmp pointer 'next' and
        rearrage all the pointers between nodes accordingly.

        When we return, we return the pointer to the previous node
        since the curr pointer would be None to exit the while
        loop.

    Runtime: O(n) since need to process each node in the list

    Memory: O(1) since we only store pointers
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next

            # Rearrange ptrs
            curr.next = prev
            prev, curr = curr, next

        return prev
