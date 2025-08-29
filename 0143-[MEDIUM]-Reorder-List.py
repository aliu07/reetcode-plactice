from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Intuition:
        We can approach this problem in 3 main steps:
        - Divide the LL into 2 halves
        - Reverse the 2nd half
        - Reorder all the nodes

        In the case of a list with an odd number of nodes, the first half will always contain
        one more element than the second half.

    Runtime:
        O(n) -> One pass to find halfway point of LL. One pass to reverse (n / 2 ~ n) second
        half of linked list. One pass to reorder.

    Memory:
        O(1) -> All modification operations are done in-place.
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Base case
        if not head or not head.next:
            return

        # Find halfway point of LL
        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None # break link

        # Reverse second half of LL
        prev, curr = None, second_half

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Modify in-place
        fst, snd = head, prev

        while fst and snd:
            fst_tmp = fst.next
            snd_tmp = snd.next

            fst.next = snd
            snd.next = fst_tmp

            fst = fst_tmp
            snd = snd_tmp
